import tensorflow as tf
import prices as price
from data_processor import DataProcessor

start = "2003-01-01"
end = "2018-01-01"

price.get_price('AAPL', start, end)

process = DataProcessor("AAPL.csv", 0.9)
process.gen_test(10)
process.gen_train(10)

X_train = process.X_train / 200
Y_train = process.Y_train / 200

X_test = process.X_test / 200
Y_test = process.Y_test / 200

model = tf.keras.models.Sequential()
model.add(tf.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.layers.Dense(1, activation=tf.nn.relu))

model.compile(optimizer="adam", loss="mean_squared_error")

model.fit(X_train, Y_train, epochs=100)
print(model.evaluate(X_test, Y_test))
