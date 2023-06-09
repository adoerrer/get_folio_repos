import unittest
from typing import List

from src.get_folio_repos.parse_okapi_install_json import modul_install_action_list_to_repository_at_tag_list, \
    ModulInstallAction

INPUT_DATA: List[ModulInstallAction] = [
    {
        "id": "mod-graphql-1.10.2",
        "action": "enable"
    },
    {
        "id": "mod-licenses-4.2.1",
        "action": "enable"
    },
    {
        "id": "mod-event-config-2.4.0",
        "action": "enable"
    },
    {
        "id": "mod-users-19.0.0",
        "action": "enable"
    },
    {
        "id": "mod-source-record-storage-5.5.2",
        "action": "enable"
    },
    {
        "id": "mod-password-validator-2.5.0",
        "action": "enable"
    },
    {
        "id": "mod-tags-1.3.0",
        "action": "enable"
    },
    {
        "id": "mod-finance-storage-8.3.1",
        "action": "enable"
    },
    {
        "id": "mod-organizations-storage-4.4.0",
        "action": "enable"
    },
    {
        "id": "mod-orders-storage-13.4.0",
        "action": "enable"
    },
    {
        "id": "mod-invoice-storage-5.5.0",
        "action": "enable"
    },
    {
        "id": "mod-permissions-6.2.0",
        "action": "enable"
    },
    {
        "id": "mod-erm-usage-4.5.1",
        "action": "enable"
    },
    {
        "id": "mod-login-7.8.0",
        "action": "enable"
    },
    {
        "id": "mod-pubsub-2.7.0",
        "action": "enable"
    },
    {
        "id": "mod-erm-usage-harvester-4.2.0",
        "action": "enable"
    },
    {
        "id": "mod-organizations-1.6.0",
        "action": "enable"
    },
    {
        "id": "mod-data-import-converter-storage-1.15.2",
        "action": "enable"
    },
    {
        "id": "mod-service-interaction-2.0.0",
        "action": "enable"
    },
    {
        "id": "mod-inventory-storage-25.0.3",
        "action": "enable"
    },
    {
        "id": "mod-inventory-update-2.3.1",
        "action": "enable"
    },
    {
        "id": "mod-circulation-storage-15.0.2",
        "action": "enable"
    },
    {
        "id": "mod-patron-blocks-1.7.1",
        "action": "enable"
    },
    {
        "id": "mod-rtac-3.4.0",
        "action": "enable"
    },
    {
        "id": "mod-user-import-3.7.1",
        "action": "enable"
    },
    {
        "id": "mod-source-record-manager-3.5.6",
        "action": "enable"
    },
    {
        "id": "mod-inventory-19.0.2",
        "action": "enable"
    },
    {
        "id": "mod-agreements-5.4.4",
        "action": "enable"
    },
    {
        "id": "mod-data-export-worker-2.0.7",
        "action": "enable"
    },
    {
        "id": "mod-quick-marc-2.5.0",
        "action": "enable"
    },
    {
        "id": "mod-authtoken-2.12.0",
        "action": "enable"
    },
    {
        "id": "mod-calendar-2.3.0",
        "action": "enable"
    },
    {
        "id": "mod-configuration-5.9.0",
        "action": "enable"
    },
    {
        "id": "mod-template-engine-1.18.0",
        "action": "enable"
    },
    {
        "id": "mod-email-1.15.2",
        "action": "enable"
    },
    {
        "id": "mod-users-bl-7.4.0",
        "action": "enable"
    },
    {
        "id": "mod-sender-1.9.0",
        "action": "enable"
    },
    {
        "id": "mod-notify-2.12.0",
        "action": "enable"
    },
    {
        "id": "mod-feesfines-18.1.1",
        "action": "enable"
    },
    {
        "id": "mod-notes-4.0.0",
        "action": "enable"
    },
    {
        "id": "mod-login-saml-2.5.0",
        "action": "enable"
    },
    {
        "id": "mod-audit-2.6.2",
        "action": "enable"
    },
    {
        "id": "mod-oai-pmh-3.10.0",
        "action": "enable"
    },
    {
        "id": "mod-finance-4.6.2",
        "action": "enable"
    },
    {
        "id": "mod-circulation-23.3.2",
        "action": "enable"
    },
    {
        "id": "mod-patron-5.4.0",
        "action": "enable"
    },
    {
        "id": "mod-ncip-1.12.2",
        "action": "enable"
    },
    {
        "id": "mod-remote-storage-1.7.1",
        "action": "enable"
    },
    {
        "id": "mod-orders-12.5.4",
        "action": "enable"
    },
    {
        "id": "mod-data-export-spring-1.5.3",
        "action": "enable"
    },
    {
        "id": "mod-invoice-5.5.0",
        "action": "enable"
    },
    {
        "id": "mod-gobi-2.5.1",
        "action": "enable"
    },
    {
        "id": "mod-ebsconet-1.4.0",
        "action": "enable"
    },
    {
        "id": "mod-eusage-reports-1.2.2",
        "action": "enable"
    },
    {
        "id": "mod-copycat-1.3.1",
        "action": "enable"
    },
    {
        "id": "mod-search-1.8.2",
        "action": "enable"
    },
    {
        "id": "mod-z3950-3.1.0",
        "action": "enable"
    },
    {
        "id": "mod-data-export-4.6.1",
        "action": "enable"
    },
    {
        "id": "mod-courses-1.4.6",
        "action": "enable"
    },
    {
        "id": "mod-ldp-1.0.7",
        "action": "enable"
    },
    {
        "id": "mod-kb-ebsco-java-3.12.2",
        "action": "enable"
    },
    {
        "id": "mod-data-import-2.6.2",
        "action": "enable"
    }
]


class NolanaReleaseCase(unittest.TestCase):
    def test_parsing(self):
        parsed_list = modul_install_action_list_to_repository_at_tag_list(INPUT_DATA)
        self.assertEqual(len(parsed_list), len(INPUT_DATA))


if __name__ == '__main__':
    unittest.main()
