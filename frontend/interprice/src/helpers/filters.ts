const filters = {
    currency(value: number) {
        const formatter = new Intl.NumberFormat('es-ES', { style: "currency", currency: "EUR" });
        if (isNaN(value)){
            return "-";
        }
        return formatter.format(value);
    },
    currencyWeight (value: number) {
        const formatter = new Intl.NumberFormat('es-ES', { style: "currency", currency: "EUR" });
        if (isNaN(value)){
            return "-";
        }
        return `${formatter.format(value)}/kg`;
    }
}

export default filters;