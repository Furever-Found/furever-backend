# Creating a generic asset class
# This will be a foundation class, but this is a rough example of it
# By default, class objects are owned by a global account object
# Class objects may be created, and owned by other accounts
# usefulness is questionable

from datetime import date


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
        def __init__(self, name: str, petId: str,
                     species: str,
                     breed: str,
                     sex: str,
                     age: int,
                     color: str,
                     date_chipped: str,
                     vaccines,
                     vet_clinic_id: str,
                     vet_fed_id: str,
                     vet_notes: str,
                     initcount: int):
            self.assetcount = initcount  # internal instance variable
            self.name = name
            self.id = petId
            self.species = species
            self.breed = breed
            self.sex = sex
            self.age = age
            self.color = color
            self.date_chipped = date_chipped
            self.vaccines = vaccines
            self.vet_clinic_id = vet_clinic_id
            self.vet_fed_id = vet_fed_id
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
        def GetAddress(self):
            return self.address

        @SagaMethod()
        def GetId(self):
            return self.id

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

    # initialized with 1 count of asset
    objloid = classvar.new(CMIConst.SPSystemAccount,
                           "Whiskers", "abcd1234",
                           "canine", "poodle",
                           "male", 2,
                           "mixed", "12/01/2021",
                           ["V1", "V2", "V3"],
                           "ClinicId1",
                           "123XYZ",
                           "some notes on the pet here"
                           1)
    objloid = objloid[0]
    #objloid1 = objloid[1]
    Log("ClsPet Object Instance: ", objloid.oid)

    #Log("ClsPet Object Instance: ", objloid1.oid)

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
