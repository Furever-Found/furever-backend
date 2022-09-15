# Creating a generic asset class
# This will be a foundation class, but this is a rough example of it
# By default, class objects are owned by a global account object
# Class objects may be created, and owned by other accounts
# usefulness is questionable

def __hdr():
    hdr = {'acct': 'aaa',
           'seq': 1000,        # whatever the next sequence number is
           'maxGU': 10,
           'feePerGU': 1,
           'extraPerGU': 2
           }
    return hdr


def __CMIClasses():

    # no signature required for creating global classes
    @SagaClass(CMIConst.SPClassObject)
    class ClsShelter:

        SagaFieldTable = []       # no user visible fields

        @SagaMethod()
        def __init__(self, name: str, address: str, description: str, initcount: int):
            self.assetcount = initcount  # internal instance variable
            self.name = name
            self.address = address
            self.description = description
            self.callcounter = 0
            self.pets = []

        @SagaMethod()
        def Increment(self, inc: int):
            self.assetcount += inc
            return self.assetcount

        @SagaMethod()
        def Decrement(self, dec: int):
            if self.assetcount - dec > 0:
                self.assetcount -= dec
                return self.assetcount
            else:
                raise RuntimeError("negative asset counts are illegal")

        @SagaMethod()
        def GetCount(self):
            return self.assetcount

        @SagaMethod()
        def GetAddress(self):
            return self.address

        # internal method - example simply counts number of calls
        def callcount(self):
            self.callcounter += 1


def __body():

    # The name ClsShelter is only available to the transaction script
    # The objectID must be retrieved if the intent is to use the class
    # log it for user to recover it, could also store it in another object
    Log("Class ClsShelter LOID: ", ClsShelter.oid)

    # An instance of the new class can be instantiated
    classvar = ClsObjVar(ClsShelter)

    # initialized with 1 count of asset
    objloid = classvar.new(CMIConst.SPSystemAccount,
                           "San Mateo Shelter", "123 Main Street, San Mateo, CA",
                           "This is a description of a nice shelter in San Mateo",
                           1)
    objloid = objloid[0]
    #objloid1 = objloid[1]
    Log("ClsShelter Object Instance: ", objloid.oid)

    #Log("ClsShelter Object Instance: ", objloid1.oid)

    objvar = ClsObjVar(objloid)

    try:
        # illegal increment the local callcounter variable. callcount is internal only
        objvar.callcount()
    except:
        pass

    count = objvar.Increment(10)

    Log("Increment Count: ", count)

    # make the objvar persistent by inserting it in the account list
    # acctvar.Insert(objvar)    # also sets owner field of objvar

    return True


def __tail():
    return {'hash': 12345,
            'sig': (rvalue, svalue)    # tuple of r and s value for signature
            }
