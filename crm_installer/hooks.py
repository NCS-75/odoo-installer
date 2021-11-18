# Copyright 2021 Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import logging

from lxml import etree

from odoo import SUPERUSER_ID, _, api, tools
from odoo.tools import file_open, load_language

_logger = logging.getLogger(__name__)

MODULE = "crm_installer"
STAGE_CONVERT = {
    "New": MODULE + ".relation_established",
    "Qualified": MODULE + ".qualified_project",
    "Proposition": MODULE + ".proposition_made",
    "Won": MODULE + ".installation_started",
}


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _logger.info(_("Removing original CRM stages..."))

    all_stage_ids = env["crm.stage"].search([])
    all_stage_xmlids = all_stage_ids.get_external_id()
    ids_to_rm = [id for id, xmlid in all_stage_xmlids.items() if MODULE not in xmlid]
    old_stage_ids = env["crm.stage"].browse(ids_to_rm)

    # Modify actual leads related to an old Stage
    old_lead_ids = (
        env["crm.lead"]
        .with_context(lang="en_US")
        .search([("stage_id", "in", old_stage_ids.ids), ("active", "in", [True, False])])
    )
    for lead_id in old_lead_ids:
        new_stage = STAGE_CONVERT.get(
            lead_id.stage_id.name, MODULE + ".relation_established"
        )
        lead_id.write({"stage_id": env.ref(new_stage).id})
    env.cr.commit()

    # Delete old stages
    old_stage_ids.unlink()
