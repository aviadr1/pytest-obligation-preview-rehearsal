from pytest_obligation import Claim, NotApplicable, ObligationContract, Profile, due_work_contract_suite
from pytest_obligation.references.in_memory import reference_derivation_binding

contract = ObligationContract(
    name="first adoption preview",
    profiles={**{p: NotApplicable("Outside this contract.") for p in Profile}, Profile.F: Claim()},
    derivation=reference_derivation_binding,
)


@due_work_contract_suite(contract)
class TestCatalog:
    pass
