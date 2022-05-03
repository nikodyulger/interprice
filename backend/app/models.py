from collections import UserList
from sqlalchemy import Column, ForeignKey, BigInteger, Integer, Float, String, Text, Date
from sqlalchemy.orm import relationship

from .database import Base


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(BigInteger, primary_key=True, index=True)
    supermarket = Column(String, primary_key=True)
    name = Column(String)
    category = Column(String)
    image_url = Column(String)
    image_url_s3 = Column(String)

    details = relationship("ProductDetails", back_populates="product", uselist=False, primaryjoin="Product.product_id == ProductDetails.product_id and Product.supermarket== ProductDetails.supermarket",lazy='joined')
    prices = relationship("ProductPrices", back_populates="product", primaryjoin="Product.product_id == ProductPrices.product_id and Product.supermarket == ProductPrices.supermarket", order_by='desc(ProductPrices.updated)')


class ProductDetails(Base):
    __tablename__ = 'product_details'

    product_id = Column(BigInteger, ForeignKey(
        "product.product_id"), primary_key=True, index=True)
    supermarket = Column(String, ForeignKey(
        "product.supermarket"), primary_key=True)
    subcategory = Column(String)
    net_qty = Column(String)
    ingredients = Column(Text)
    storage = Column(Text)
    preparation = Column(Text)
    manufacturer = Column(Text)

    product = relationship("Product", back_populates='details', primaryjoin="Product.product_id == ProductDetails.product_id and Product.supermarket== ProductDetails.supermarket", lazy='joined')


class ProductPrices(Base):
    __tablename__ = 'product_prices'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(BigInteger, ForeignKey("product.product_id"))
    supermarket = Column(String, ForeignKey("product.supermarket"))
    price = Column(Float)
    price_per_unit = Column(Float)
    updated = Column(Date)

    product = relationship("Product", back_populates='prices', primaryjoin="Product.product_id == ProductPrices.product_id and Product.supermarket == ProductPrices.supermarket")
