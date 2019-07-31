from smbus2 import SMBusWrapper

with SMBusWrapper(1) as bus:
	# Read a block of 6 bytes from address 8, offset 0
	block = bus.read_i2c_block_data(8, 0, 6)
	# Returned value is a list of 16 bytes
	print(block)
	print(''.join( chr(x) for x in block))