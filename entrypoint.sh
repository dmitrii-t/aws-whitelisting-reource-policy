#!/bin/sh

# The following runs once local volume is mounted

pulumi login file://~ && pulumi plugin install resource aws v2.5.0

pulumi ${@:-}