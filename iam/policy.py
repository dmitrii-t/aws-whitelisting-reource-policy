import json

import pulumi
import pulumi_aws as aws

config = pulumi.Config()

caller_identity = aws.get_caller_identity()

account_id = caller_identity.account_id


def get_identity_policy_document() -> str:
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Resource": "*",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret",
                "secretsmanager:ListSecrets",
                "secretsmanager:ListSecretVersionIds",

                "kms:*"
            ]
        }]
    })


def get_assume_role_policy_document() -> str:
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "AWS": f"{account_id}"
            }
        }]
    })


def get_secret_resource_policy_document(trusted_role_unique_id: str) -> str:
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Deny",
            "Resource": "*",
            "Principal": "*",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Condition": {
                "StringNotLike": {
                    "aws:userId": [
                        f"{trusted_role_unique_id}:*",

                        f"{caller_identity.user_id}",
                        f"{account_id}"
                    ]
                }
            }
        }]
    })
