import logging
import pymysql
import json
import os
import boto3


def data_pipeline(event, context):

    # Parameters to connect with AWS RDS Aurora
    host = os.environ['RDS_HOST']
    name = os.environ['NAME']
    password = os.environ['PASSWORD']
    db_name = os.environ['DB_NAME']

    # Other paramaters
    s3_image_url = os.environ['S3_IMAGE_URL']

    # Setting the log
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Initialize counters
    new_items, changed_rows = 0,0

    # Setting SNS client
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']
    sns = boto3.client('sns')

    # S3 Object management to process data from
    bucket = 'supermarkets-interprice'
    key = f"data/{event['queryStringParameters']['key']}.json"

    logger.info(
        f"INFO: Data Pipeline - {event['queryStringParameters']['key']}")

    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        data = json.loads(response['Body'].read())
    except Exception as e:
        logger.error("ERROR: Could not retrieve file from S3 Bucket")
        logger.error(e)
        message = {
            "statusCode": 200,
            "body": "ERROR: Could not retrieve file from S3 Bucket"
        }
        return "ERROR: Could not retrieve file from S3 Bucket"

    try:
        conn = pymysql.connect(host=host,
                               user=name,
                               password=password,
                               db=db_name,
                               connect_timeout=5)
    except pymysql.MySQLError as e:
        logger.error("ERROR: Could not connect to AWS Aurora instance")
        logger.error(e)
        message = {
            "statusCode": 200,
            "body": "ERROR: Could not connect to AWS Aurora instance"
        }
        return "ERROR: Could not connect to AWS Aurora instance"

    logger.info("SUCCES: Connection to AWS RDS Aurora instance succeded")

    with conn.cursor() as cur:
        for product in data:

            try:
                query = """INSERT INTO product (product_id, supermarket, name, category, image_url, image_url_s3) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
                cur.execute(query,
                            (product['product_id'], product['supermarket'], product['name'],
                             product['category'], product['image_urls'][0], f"{s3_image_url}{product['images'][0]['path']}")
                            )
                logger.info(
                    f"Product ({product['product_id']},'{product['supermarket']}') inserted")
                new_items += 1 
            except pymysql.err.MySQLError:
                query = """INSERT INTO product (product_id, supermarket, name, category, image_url,image_url_s3) 
                    VALUES (%s, %s, %s, %s,%s,%s) 
                    ON DUPLICATE KEY UPDATE 
                        name = %s,
                        category = %s,
                        image_url = %s,
                        image_url_s3 = %s"""

                cur.execute(query,
                            (product['product_id'], product['supermarket'], product['name'], product['category'], product['image_urls'][0],
                                product['images'][0]['path'], product['name'], product['category'], product['image_urls'][0], f"{s3_image_url}{product['images'][0]['path']}")
                            )

                logger.info(
                    f"Product ({product['product_id']},'{product['supermarket']}') already exists, so it's updated")
                changed_rows += 1

            conn.commit()

            if len(product) > 9:
                try:
                    query = """INSERT INTO product_details (product_id, supermarket, subcategory, net_qty, ingredients, storage, preparation, manufacturer)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    cur.execute(query,
                                (product['product_id'], product['supermarket'], product['subcategory'], product['net_qty'],
                                 product['ingredients'], product['storage'], product['preparation'], product['manufacturer'])
                                )
                    logger.info(
                        f"Product ({product['product_id']},'{product['supermarket']}') details inserted")
                except pymysql.err.MySQLError:
                    query = """INSERT INTO product_details (product_id, supermarket, subcategory, net_qty, ingredients, storage, preparation, manufacturer)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            subcategory = %s,
                            net_qty = %s,
                            ingredients = %s,
                            storage = %s,
                            preparation = %s,
                            manufacturer = %s"""
                    cur.execute(query,
                                (product['product_id'], product['supermarket'], product['subcategory'], product['net_qty'], product['ingredients'], product['storage'], product['preparation'],
                                 product['manufacturer'], product['subcategory'], product['net_qty'], product['ingredients'], product['storage'], product['preparation'], product['manufacturer'])
                                )
                    logger.info(
                        f"Product details({product['product_id']},'{product['supermarket']}') already exists, so they are updated")

            conn.commit()

            query = """INSERT INTO product_prices (product_id, supermarket, price, price_per_unit, updated)
                VALUES (%s, %s, %s, %s, %s)"""

            cur.execute(
                query,
                (product['product_id'], product['supermarket'],
                 product['price'], product['price_per_unit'], product['last_updated'])
            )

            conn.commit()

        cur.close()

    conn.commit()
    conn.close()

    message = {
        "statusCode": 200,
        "body": json.dumps({
            "msg": "Everything when OK!!",
            "new_items": new_items,
            "changed_rows": changed_rows
        })
    }
    response = sns.publish(
        TopicArn=sns_topic_arn,
        Message=json.dumps(message)
    )

    return {
        "statusCode": 200,
        "body": json.dumps('Everything went OK!!')
    }
