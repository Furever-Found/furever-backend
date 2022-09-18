# furever-backend

Back-end SagaPython code for the **Furever Found** web3athon submission.

## Summary
This repo is the starting point for developing Accounts and Assets for the Furever Found project.

Much of the code written here relies on the fact that saga python is a pre-alpha repo. Most version of th code do not compile;
Renaming classes slows down the compilation by a factor of 20. Adding new fields increases this by an order of multitude.

Simply opening up the `classassetexample.ps` file and allowing the VS formatting extention to do it's work makes the compilation/execution time go up by a factor of 20.

Adding a second set of public Get/Set methods ads another 360 seconds to the execution time.
Adding a third adds 1,300 seconds.
Adding a fourth stalls the machine completely.

These details have made testing difficult, but should be noted for future development.

For this repo, 3 classes have been created:

- `ClsPet` - an asset representing an adopted pet, that can be attached to both a ClsShelter and ClsOwner accounts.
- `ClsShelter` - should be an account representing an individual pet shelter. No examples of how to do this exist, so it's currently declared as an asset.
- `ClsOwner` - should be an account representing an individual pet shelter. No examples of how to do this exist, so it's currently declared as an asset.

# Setup

SagaPython executions create `.db` and `.txt` files that need to be cleared out before the next run. The script `fur.sh` takes care of this issue and should be run prior to every execution.

# Execution

The commands used to execute the code are listed below; I am including the `time` command before the `python3` command to evaluate the execution time (the timings listed above have been gathered using this detail.)

## File locations

The contents of this repo should be placed in a folder on the same level as `SagaPython` and `SagaChain`. The commands should be run from the `SagaPython` folder.

## Commands

### Pets

The pets asset can be created with the following command:

`time python3 sagapythonclasses.py ../furever-backend/clspet.py `

The expected response would be something like :

`python3 sagapythonclasses.py ../furever-backend/clspet.py 168.72s user 0.32s system 99% cpu 2:49.21 total`

Any call to `sagapythonclasses.py` would generate a collection of `*.db` files in the `SagaPython` folder, and would log some output to the `sptransactionlog.txt` file.
These have to be cleared out before the next time a call is made; this is done with the script `fur.sh` mentioned above.

### Shelters

The `shelters` asset can be created with the following command:

`time python3 sagapythonclasses.py ../furever-backend/classclsshelter.py `

The expected response would be something like :

`python3 sagapythonclasses.py ../furever-backend/classclsshelter.py 2649.26s user 11.89s system 99% cpu 44:30.02 total`

#### Adding pets to a shelter

Until the account/asset explanations are in place, the current way to add a pet to a shelter would be through the `AddPet(self, petId: str)` method.

The way to retrieve pets is through the `def GetPets(self)` method.

### Pet Owners

The `ClsPetOwners` asset can be created with the following command:

`time python3 sagapythonclasses.py ../furever-backend/classclspetowner.py `

The expected response would be something like :

`python3 sagapythonclasses.py ../furever-backend/classclspetowner.py 2649.26s user 11.89s system 99% cpu 44:30.02 total`

#### Adding pets to a pet owner

Until the account/asset explanations are in place, the current way to add a pet to an owner would be through the `AddPet(self, petId: str)` method.

The way to retrieve pets is through the `def GetPets(self)` method.

## Logging

Logging has been used in every class to examine the data that is being processed; currently, everything gets saved to the
default file (established by `PraSaga`, in the `SagaPython` folder), and named `sptransactionlog.txt`. Logs can be examined after every execution.
This file will get re-initialized after every run.
