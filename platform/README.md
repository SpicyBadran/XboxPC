# Platform — UEFI Diagnostic Probe (Phase 6)

Modular inventories, each owning one concern. No monolithic `main.c`.

| Module | Responsibility |
|--------|----------------|
| `uefi-probe/` | EFI entry point, boot services, exit/reboot handling |
| `cpu-inventory/` | CPUID, vendor, brand, family/model/stepping, topology, ISA, virtualization |
| `memory-inventory/` | UEFI memory map, descriptors, reserved ranges |
| `pci-inventory/` | PCI BDF enumeration, vendor/device/class, topology |
| `gpu-inventory/` | GPU PCI IDs, GOP, display modes (no full driver claim) |
| `storage-inventory/` | NVMe/SATA/USB via Block I/O, read-only |
| `firmware-inventory/` | UEFI revision, ACPI, SMBIOS, Secure Boot state |

Placeholder Phase 0 — implementation authorized only after Phase 5 approval (see `ENGINEERING_RULES.md` 3.6).

Each module exports `efi_status_t inventory_<module>(report_context *ctx)` and is unit-testable.
