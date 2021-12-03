PARTNERS
========

**READ**

.. code-block:: bash

  # All
  curl -X GET "https://erp.dualsun.com/crm-api/partner" \
      -H "accept: application/json"
      -H  "API-KEY: 123456789" \
  # All records updated since a given date
  curl -X GET "https://erp.dualsun.com/crm-api/partner/?write_date_from=2021-01-30" \
      -H "accept: application/json"
      -H  "API-KEY: 123456789" \
  # All records updated *manually* since a given date
  curl -X GET "https://erp.dualsun.com/crm-api/partner/?manual_write_date_from=2021-01-30" \
      -H "accept: application/json"
      -H  "API-KEY: 123456789" \
  # One (id = 10)
  curl -X GET "https://erp.dualsun.com/crm-api/partner/10" \
      -H "accept: application/json" \
      -H  "API-KEY: 123456789" \
  # By Incwo ID (contacts only)
  curl -X GET "https://erp.dualsun.com/crm-api/partner/789456/incwo_contact" \
      -H "accept: application/json" \
      -H  "API-KEY: 123456789" \
  # By Incwo ID (companies only)
  curl -X GET "https://erp.dualsun.com/crm-api/partner/987654/incwo_company" \
      -H "accept: application/json" \
      -H  "API-KEY: 123456789" \

**UPDATE**

.. code-block:: bash

  curl -X POST "https://erp.dualsun.com/crm-api/partner/13" \
      -H "API-KEY: 123456789" \
      -H  "accept: application/json" \
      -H  "Content-Type: application/json" \
      --data '{"comment": "Updated comment from API in partner (id=13)"}'


**CREATE**

.. code-block:: bash

  curl -X POST "https://erp.dualsun.com/crm-api/partner/" \
      -H "API-KEY: 123456789" \
      -H  "accept: application/json" \
      -H  "Content-Type: application/json" \
      --data '{"name": "New test partner created from API", "city": "errejota", "street": "Rua Marielle Franco", "zip_code": "12345"}'

**ARCHIVE (DELETE)**

.. code-block:: bash

  curl -X POST "https://erp.dualsun.com/crm-api/partner/53/archive" \
      -H "API-KEY: 123456789" \
      -H  "accept: */*"


CRM LEADS
=========

**READ**

.. code-block:: bash

  # All
  curl -X GET "https://erp.dualsun.com/crm-api/lead" \
      -H "accept: application/json"
      -H  "API-KEY: 123456789" \
  # All records updated since a given date
  curl -X GET "https://erp.dualsun.com/crm-api/lead/?write_date_from=2021-01-30" \
      -H "accept: application/json"
      -H  "API-KEY: 123456789" \
  # All records updated *manually* since a given date
  curl -X GET "https://erp.dualsun.com/crm-api/lead/?manual_write_date_from=2021-01-30" \
      -H "accept: application/json"
      -H  "API-KEY: 123456789" \
  # One (id = 18)
  curl -X GET "https://erp.dualsun.com/crm-api/lead/18" \
      -H "accept: application/json" \
      -H  "API-KEY: 123456789" \
  # By Incwo ID
  curl -X GET "https://erp.dualsun.com/crm-api/lead/789456/incwo" \
      -H "accept: application/json" \
      -H  "API-KEY: 123456789" \


**UPDATE**

.. code-block:: bash

  curl -X POST "https://erp.dualsun.com/crm-api/lead/18" \
      -H "API-KEY: 123456789" \
      -H  "accept: application/json" \
      -H  "Content-Type: application/json" \
      --data '{"summary": "Updated description from API in lead (id=18)"}'

**CREATE**

.. code-block:: bash

  curl -X POST "https://erp.dualsun.com/crm-api/lead" \
      -H "API-KEY: 123456789" \
      -H  "accept: application/json" \
      -H  "Content-Type: application/json" \
      --data '{"type": "opportunity", "name": "Test Lead created from API", "city": "errejota", "street": "Rua Marielle Franco", "zip_code": "12345"}'

**ARCHIVE (DELETE)**

.. code-block:: bash

  curl -X POST "https://erp.dualsun.com/crm-api/lead/53/archive" \
      -H "API-KEY: 123456789" \
      -H  "accept: */*"

Points d'API sous forme de liste
=========

.. code-block:: python

  lang # List m2o
  ["en_US", "fr_FR", "de_DE", "es_ES", "it_IT", "nl_NL", "pt_PT"]

  country_code # List m2o - Code ISO 3166-2, 2 digits
  ["FR", "IT", "GB", ...]

  role_name # List m2o
  ["Installer", "Distributor", "Project Manager", "End Customer", "Project Owner"]

  relation_code # List m2o
  ["0", "1", "2", "3", "4"]

  distributor_ids # List m2m ids with domain
  [("is_distributor", "=", True), ("is_company", "=", True)]

  range_names # List m2m names
  ["Residential (< 9kWc)", "Commercial (> 9kWc)"]

  use_names # List m2m names
  ["Water Heater", "Swiming-pool", "Heating"]

  heater_names # List m2m names
  ["Electrical Resistance", "Heat Pump air/water", "Heat Pump water/water", "Gas boiler", "Wood boiler", "Oil boiler", "District Heating", "Thermodynamic Water Heater"]

  lost_reason_name # List m2o names
  ["No answer", "Meeting cancelled", ...]
  # N-B: Use {"lost_reason_name": ""} to reactivate a lost lead

  phase # Selection list
  ["aps", "apd", "pro", "dce"]

  building_name # List m2o names
  ["House", "Hotel", ...]
