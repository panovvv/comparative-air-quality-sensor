EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr User 7795 5512
encoding utf-8
Sheet 1 1
Title "PPD42 module for Comparative air quality sensor"
Date "2020-03-29"
Rev "1"
Comp "Vadim Panov"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L bluepill:BP U1
U 1 1 5CCD5CBA
P 3550 2100
F 0 "U1" H 3550 3350 60  0000 C CNN
F 1 "BP" H 3550 3244 60  0000 C CNN
F 2 "" H 3450 2850 60  0001 C CNN
F 3 "" H 3450 2850 60  0001 C CNN
	1    3550 2100
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Female J1
U 1 1 5CCD5DB6
P 1400 2050
F 0 "J1" H 1294 2335 50  0000 C CNN
F 1 "SP16-4p" H 1294 2244 50  0000 C CNN
F 2 "" H 1400 2050 50  0001 C CNN
F 3 "~" H 1400 2050 50  0001 C CNN
	1    1400 2050
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1600 1950 1850 1950
Wire Wire Line
	2300 1950 2300 1800
Wire Wire Line
	1600 2050 2300 2050
Wire Wire Line
	1600 2150 2300 2150
Wire Wire Line
	1600 2250 1850 2250
Wire Wire Line
	2300 2250 2300 2400
$Comp
L power:GND #PWR02
U 1 1 5CCD6218
P 2300 2400
F 0 "#PWR02" H 2300 2150 50  0001 C CNN
F 1 "GND" H 2305 2227 50  0000 C CNN
F 2 "" H 2300 2400 50  0001 C CNN
F 3 "" H 2300 2400 50  0001 C CNN
	1    2300 2400
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR01
U 1 1 5CCD627B
P 2300 1800
F 0 "#PWR01" H 2300 1650 50  0001 C CNN
F 1 "+5V" H 2315 1973 50  0000 C CNN
F 2 "" H 2300 1800 50  0001 C CNN
F 3 "" H 2300 1800 50  0001 C CNN
	1    2300 1800
	1    0    0    -1  
$EndComp
Text Label 2300 2050 2    50   ~ 0
SDA
Text Label 2300 2150 2    50   ~ 0
SCL
$Comp
L power:GND #PWR06
U 1 1 5CCD63DC
P 5050 2450
F 0 "#PWR06" H 5050 2200 50  0001 C CNN
F 1 "GND" H 5055 2277 50  0000 C CNN
F 2 "" H 5050 2450 50  0001 C CNN
F 3 "" H 5050 2450 50  0001 C CNN
	1    5050 2450
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR05
U 1 1 5CCD63ED
P 4950 1750
F 0 "#PWR05" H 4950 1600 50  0001 C CNN
F 1 "+5V" H 4965 1923 50  0000 C CNN
F 2 "" H 4950 1750 50  0001 C CNN
F 3 "" H 4950 1750 50  0001 C CNN
	1    4950 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 2100 4950 2100
Wire Wire Line
	4950 2100 4950 1750
Wire Wire Line
	5150 1900 5050 1900
Wire Wire Line
	5050 1900 5050 2450
Wire Wire Line
	4700 2900 4300 2900
$Comp
L power:GND #PWR04
U 1 1 5CCD6761
P 3700 3300
F 0 "#PWR04" H 3700 3050 50  0001 C CNN
F 1 "GND" H 3705 3127 50  0000 C CNN
F 2 "" H 3700 3300 50  0001 C CNN
F 3 "" H 3700 3300 50  0001 C CNN
	1    3700 3300
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR03
U 1 1 5CCD6772
P 3700 850
F 0 "#PWR03" H 3700 700 50  0001 C CNN
F 1 "+5V" H 3715 1023 50  0000 C CNN
F 2 "" H 3700 850 50  0001 C CNN
F 3 "" H 3700 850 50  0001 C CNN
	1    3700 850 
	1    0    0    -1  
$EndComp
Wire Wire Line
	3700 850  3700 1050
Wire Wire Line
	3700 3150 3700 3300
Wire Wire Line
	4300 1500 4500 1500
Wire Wire Line
	4300 1600 4500 1600
Text Label 4500 1500 2    50   ~ 0
SDA
Text Label 4500 1600 2    50   ~ 0
SCL
$Comp
L Sensor_Gas_Homemade:PPD42 S1
U 1 1 5E809B92
P 5500 2100
F 0 "S1" H 5728 2146 50  0000 L CNN
F 1 "PPD42" H 5728 2055 50  0000 L CNN
F 2 "" H 5450 2050 50  0001 C CNN
F 3 "https://www.mouser.com/datasheet/2/744/Seeed_101020012-1217636.pdf" H 5450 2050 50  0001 C CNN
	1    5500 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 2000 4700 2000
Wire Wire Line
	4700 2000 4700 2900
Wire Wire Line
	5150 2200 4500 2200
Wire Wire Line
	4500 2200 4500 2800
Wire Wire Line
	4500 2800 4300 2800
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 5E8162EB
P 1850 1950
F 0 "#FLG0101" H 1850 2025 50  0001 C CNN
F 1 "PWR_FLAG" H 1850 2123 50  0000 C CNN
F 2 "" H 1850 1950 50  0001 C CNN
F 3 "~" H 1850 1950 50  0001 C CNN
	1    1850 1950
	1    0    0    -1  
$EndComp
Connection ~ 1850 1950
Wire Wire Line
	1850 1950 2300 1950
$Comp
L power:PWR_FLAG #FLG0102
U 1 1 5E816A45
P 1850 2250
F 0 "#FLG0102" H 1850 2325 50  0001 C CNN
F 1 "PWR_FLAG" H 1850 2423 50  0000 C CNN
F 2 "" H 1850 2250 50  0001 C CNN
F 3 "~" H 1850 2250 50  0001 C CNN
	1    1850 2250
	-1   0    0    1   
$EndComp
Connection ~ 1850 2250
Wire Wire Line
	1850 2250 2300 2250
NoConn ~ 4300 1300
NoConn ~ 4300 1400
NoConn ~ 4300 1700
NoConn ~ 4300 1800
NoConn ~ 4300 1900
NoConn ~ 4300 2000
NoConn ~ 4300 2100
NoConn ~ 4300 2200
NoConn ~ 4300 2300
NoConn ~ 4300 2400
NoConn ~ 4300 2500
NoConn ~ 4300 2600
NoConn ~ 4300 2700
NoConn ~ 2800 2900
NoConn ~ 2800 2700
NoConn ~ 2800 2600
NoConn ~ 2800 2500
NoConn ~ 2800 2400
NoConn ~ 2800 2300
NoConn ~ 2800 2200
NoConn ~ 2800 2100
NoConn ~ 2800 2000
NoConn ~ 2800 1900
NoConn ~ 2800 1800
NoConn ~ 2800 1700
NoConn ~ 2800 1600
NoConn ~ 2800 1500
NoConn ~ 2800 1400
NoConn ~ 2800 1300
NoConn ~ 3400 1050
NoConn ~ 3550 1050
NoConn ~ 3400 3150
NoConn ~ 3500 3150
NoConn ~ 5150 2300
$EndSCHEMATC
