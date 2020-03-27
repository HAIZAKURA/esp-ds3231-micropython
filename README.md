# esp-ds3231-micropython
[![Author](https://img.shields.io/badge/Author-HAIZAKURA-b68469?style=flat-square)](https://nya.run) [![License](https://img.shields.io/github/license/HAIZAKURA/esp-ds3231-micropython?style=flat-square)](./LICENSE)

A DS3231 Lib for esp8266/esp32 with MicroPython.

If you are using pyboard or another board, please modify the usage of `Pin` and `I2C` in `ds3231.py` .

## Usage

```python
from ds3231 import DS3231

ds = DS3231(sdapin=18, sclpin=19)

# get year
ds.year()
# set year
ds.year(2020)

# get month
ds.month()
# set month
ds.month(3)

# get day
ds.day()
# set day
ds.day(27)

# get hour
ds.hour()
# set hour
ds.hour(17)

# get minute
ds.min()
# set minute
ds.min(16)

# get second
ds.sec()
# set second
ds.sec(45)

# get time
# [17, 16, 45]
ds.time()
# set time
ds.time(17, 16, 45)

# get date
# [2020, 3, 27]
ds.date()
# set date
ds.date(2020, 3, 27)

# get datetime
# [2020, 3, 27, 17, 16, 45]
ds.datetime()
# set datetime
ds.datetime(2020, 3, 27, 17, 16, 45)

# get temperature
ds.temp()
```

## Notice

The `build/ds3231.mpy` is a compiled bytecode file, and only can be used in `MicroPython v1.12+` .

## Author

**esp-ds3231-micropython** © [HAIZAKURA](https://nya.run), Released under the [MIT](./LICENSE) License.

> [Personal Website](https://nya.run) · GitHub [@HAIZAKURA](https://github.com/HAIZAKURA) · Twitter [@haizakura_0v0](https://twitter.com/haizakura_0v0) · Telegram [@haizakura](https://t.me/haizakura)