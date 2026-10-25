from pytest_obligation import Claim, NotApplicable, ObligationContract, Profile, due_work_contract_suite
from pytest_obligation.references.in_memory import (
    EdgeTriggeredDeriver,
    materialising_derivation_binding,
    reference_derivation_binding,
)

contract = ObligationContract(
    name="first adoption preview",
    profiles={**{p: NotApplicable("Outside this contract.") for p in Profile}, Profile.F: Claim()},
    derivation=reference_derivation_binding,
)


@due_work_contract_suite(contract)
class TestCatalog:
    pass


# This implementation never derives an obligation from desired state. Its binding
# passes the ownership guard, but the generated profile-F contract tests fail.
broken_contract = ObligationContract(
    name="broken derivation: desired work is never discovered",
    profiles={**{p: NotApplicable("Outside this contract.") for p in Profile}, Profile.F: Claim()},
    derivation=lambda: materialising_derivation_binding(EdgeTriggeredDeriver()),
)


@due_work_contract_suite(broken_contract)
class TestBrokenDerivation:
    pass
