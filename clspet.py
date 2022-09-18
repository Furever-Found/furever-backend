# Creating an asset class representing a pet;
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
    class ClsPet:

        SagaFieldTable = []       # no user visible fields

        @SagaMethod()
        def __init__(self, name: str, initcount: int):
            self.assetcount = initcount  # internal instance variable
            self.name = name
            self.callcounter = 0

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
        def GetName(self):
            return self.name

        @SagaMethod()
        def GetSpecies(self):
            return self.species

        @SagaMethod()
        def SetSpecies(self, species: str):
            self.species = species

        # internal method - example simply counts number of calls

        def callcount(self):
            self.callcounter += 1


def __body():

    # The name ClsPet is only available to the transaction script
    # The objectID must be retrieved if the intent is to use the class
    # log it for user to recover it, could also store it in another object
    Log("Class ClsPet LOID: ", ClsPet.oid)

    # An instance of the new class can be instantiated
    classvar = ClsObjVar(ClsPet)

    # initialized with 100 count of asset
    objloid = classvar.new(CMIConst.SPSystemAccount, "Whiskers", 1)
    objloid = objloid[0]
    Log("ClsPet Object Instance: ", objloid.oid)

    objvar = ClsObjVar(objloid)
    objvar.SetSpecies("cat")

    try:
        # illegal increment the local callcounter variable. callcount is internal only
        objvar.callcount()
    except:
        pass

    Log("Name: ", objvar.GetName(), ", species: ", objvar.GetSpecies())

    # make the objvar persistent by inserting it in the account list
    # acctvar.Insert(objvar)    # also sets owner field of objvar

    return True


def __tail():
    return {'hash': 12345,
            'sig': (rvalue, svalue)    # tuple of r and s value for signature
            }
