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
def broken_derivation_binding():
    # ARRANGE: create a fresh in-memory domain with desired state but no records.
    deriver = EdgeTriggeredDeriver()
    # REAL PRODUCTION: bind the library's deliberately broken derive implementation.
    # EXTERNAL SEAM: none; all state belongs to this in-memory reference domain.
    # OBSERVE: outstanding and record_of expose whether desired work was discovered.
    return materialising_derivation_binding(deriver)


broken_contract = ObligationContract(
    name="broken derivation: desired work is never discovered",
    profiles={**{p: NotApplicable("Outside this contract.") for p in Profile}, Profile.F: Claim()},
    derivation=broken_derivation_binding,
)


@due_work_contract_suite(broken_contract)
class TestBrokenDerivation:
    pass
