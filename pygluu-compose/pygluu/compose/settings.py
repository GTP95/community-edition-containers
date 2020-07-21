DEFAULT_SETTINGS = {
    "HOST_IP": "",
    "DOMAIN": "",
    "ADMIN_PW": "",
    "LDAP_PW": "",
    "REDIS_PW": "",
    "REDIS_URL": "redis:6379",
    "REDIS_TYPE": "STANDALONE",
    "REDIS_USE_SSL": False,
    "REDIS_SSL_TRUSTSTORE": "",
    "REDIS_SENTINEL_GROUP": "",
    "EMAIL": "",
    "ORG_NAME": "",
    "COUNTRY_CODE": "",
    "STATE": "",
    "CITY": "",
    "SVC_LDAP": True,
    "SVC_OXAUTH": True,
    "SVC_OXTRUST": True,
    "SVC_OXPASSPORT": False,
    "SVC_OXSHIBBOLETH": False,
    "SVC_CR_ROTATE": False,
    "SVC_KEY_ROTATION": False,
    "SVC_OXD_SERVER": False,
    "SVC_RADIUS": False,
    "SVC_REDIS": False,
    "SVC_VAULT_AUTOUNSEAL": False,
    "SVC_CASA": False,
    "SVC_JACKRABBIT": False,
    "SVC_SCIM": False,
    "SVC_FIDO2": False,
    "PERSISTENCE_TYPE": "ldap",
    "CACHE_TYPE": "NATIVE_PERSISTENCE",
    "PERSISTENCE_LDAP_MAPPING": "default",
    "PERSISTENCE_VERSION": "4.2.0_01",
    "CONFIG_INIT_VERSION": "4.2.0_01",
    "COUCHBASE_USER": "admin",
    "COUCHBASE_URL": "localhost",
    "OXTRUST_API_ENABLED": False,
    "OXTRUST_API_TEST_MODE": False,
    "PASSPORT_ENABLED": False,
    "CASA_ENABLED": False,
    "RADIUS_ENABLED": False,
    "SAML_ENABLED": False,
    "SCIM_ENABLED": False,
    "SCIM_TEST_MODE": False,
    "ENABLE_OVERRIDE": False,
    "PERSISTENCE_SKIP_EXISTING": True,
    "DOCUMENT_STORE_TYPE": "LOCAL",
}

COMPOSE_MAPPINGS = {
    "SVC_LDAP": "svc.ldap.yml",
    "SVC_OXAUTH": "svc.oxauth.yml",
    "SVC_OXTRUST": "svc.oxtrust.yml",
    "SVC_OXPASSPORT": "svc.oxpassport.yml",
    "SVC_OXSHIBBOLETH": "svc.oxshibboleth.yml",
    "SVC_CR_ROTATE": "svc.cr_rotate.yml",
    "SVC_KEY_ROTATION": "svc.key_rotation.yml",
    "SVC_OXD_SERVER": "svc.oxd_server.yml",
    "SVC_RADIUS": "svc.radius.yml",
    "SVC_REDIS": "svc.redis.yml",
    "SVC_VAULT_AUTOUNSEAL": "svc.vault_autounseal.yml",
    "SVC_CASA": "svc.casa.yml",
    "SVC_JACKRABBIT": "svc.jackrabbit.yml",
    "SVC_SCIM": "svc.scim.yml",
    "SVC_FIDO2": "svc.fido2.yml",
    "ENABLE_OVERRIDE": "docker-compose.override.yml",
}
