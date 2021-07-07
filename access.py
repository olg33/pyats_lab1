#!/usr/bin/python3.8
__author__ = "Oscar Lopez (oscar.lopez@anuvu.com)"
__version__ = ": 1.0 "
__date__ = "7/7/21"
__copyright__ = "Copyright (c) 2021 OL"
__license__ = "Python"

from genie.testbed import load
import json

def main():

    # Instantiate the Testbed
    testbed = load('/home/administrator/pyats/lab_1/testbed1.yaml')
    #print(f"\n======= TESTBED INFO =======\n")
    #print(f"\tTestbed Value (object): {testbed}")
    #print(f"\n======= END TESTBED INFO =======\n")

    # MIR-LAB NXOS Device
    device = testbed.devices['GE_HUB1_INT_SW1.MIR']
    device.connect()
    response = device.parse('show version') 
    #print(f"\nResponse from testbed1 is of type {type(response)} and length {len(response)}")
    print(response)
    print(json.dumps(response, indent=4))
    #print(response.keys())

    # MIR-LAB IOS-XE Device
    device = testbed.devices['GE_HUB1_INT_HRT1.MIR']
    device.connect()
    response = device.parse('show version') 
    #print(f"\nResponse from testbed1 is of type {type(response)} and length {len(response)}")
    print(response)    
    print(json.dumps(response, indent=4))
    print(response.keys())
     
# Standard call to the main() function.
if __name__ == '__main__':
    main()
