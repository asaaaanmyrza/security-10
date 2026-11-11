import os
import hvac

client = hvac.Client(
    url=os.environ.get("VAULT_ADDR", "http://127.0.0.1:8200"),
    token=os.environ["VAULT_TOKEN"],
)
secrets = client.secrets.kv.v2.read_secret_version(
    path="myapp", mount_point="secret"
)["data"]["data"]

print("Секреты получены из Vault:", list(secrets.keys()))
print("SECRET_KEY =", secrets["SECRET_KEY"])
