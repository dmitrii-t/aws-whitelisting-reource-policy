import json

import pulumi
import pulumi_aws as aws

config = pulumi.Config()

switch_role_username = config.require('username')

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

                "kms:ListKey*"
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
                "AWS": f"arn:aws:iam::{account_id}:user/{switch_role_username}"
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
                        f"{account_id}"
                    ]
                }
            }
        }]
    })
