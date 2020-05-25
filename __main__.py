import json

import pulumi
from pulumi_aws import secretsmanager, iam

from iam.policy import get_identity_policy_document, get_assume_role_policy_document, \
    get_secret_resource_policy_document

noaccess_role = iam.Role("noaccess-role",
                         name="NoAccessRole",
                         assume_role_policy=get_assume_role_policy_document())

trusted_role = iam.Role("trusted-role",
                        name="TrustedRole",
                        assume_role_policy=get_assume_role_policy_document())

identity_policy = iam.Policy("identity-policy",
                             name="IdentityPolicy",
                             policy=get_identity_policy_document())

noaccess_role_attachment = iam.RolePolicyAttachment("noaccess-role-attachment",
                                                    role=noaccess_role,
                                                    policy_arn=identity_policy.arn)

trusted_role_attachment = iam.RolePolicyAttachment("trusted-role-attachment",
                                                   role=trusted_role,
                                                   policy_arn=identity_policy.arn)

secret_resource_policy_document = trusted_role.unique_id.apply(lambda it: get_secret_resource_policy_document(it))

secret = secretsmanager.Secret("secret",
                               name="Secret",
                               policy=secret_resource_policy_document)

secret_value = secretsmanager.SecretVersion("secret-vale",
                                            secret_id=secret.arn,
                                            secret_string=json.dumps({
                                                "database_connection_url": ""
                                            }))

# Outputs
pulumi.export('trusted_role_arn', trusted_role.arn)
pulumi.export('noaccess_role_arn', noaccess_role.arn)
pulumi.export('secret_arn', secret.arn)
pulumi.export('secret_resource_policy', secret_resource_policy_document)
