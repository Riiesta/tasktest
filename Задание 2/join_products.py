from pyspark.sql import SparkSession
from pyspark.sql import Row

# Инициализация SparkSession
spark = SparkSession.builder \
    .appName("Product and Categories Join") \
    .master("local") \
    .getOrCreate()

# Создание датафреймов из Row объектов
products = spark.createDataFrame([
    Row(product_id=1, product_name="Product A"),
    Row(product_id=2, product_name="Product B")
])

categories = spark.createDataFrame([
    Row(category_id=1, category_name="Category X"),
    Row(category_id=2, category_name="Category Y")
])

product_categories = spark.createDataFrame([
    Row(product_id=1, category_id=1),
    Row(product_id=2, category_id=1),
    Row(product_id=2, category_id=2)
])

# Отображение изначальных датафреймов
print("Products DataFrame:")
products.show()

print("Categories DataFrame:")
categories.show()

print("Product-Categories DataFrame:")
product_categories.show()

# Соединение датафреймов
joined_df = products.join(product_categories, "product_id", "left_outer") \
    .join(categories, "category_id", "left_outer") \
    .select("product_name", "category_name")

# Отображение результата соединения
print("Result of the Join:")
joined_df.show()

# Завершение сессии
spark.stop()
