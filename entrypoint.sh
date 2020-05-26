#!/bin/sh

pulumi login file://~

pulumi plugin install resource aws v2.5.0

pulumi ${@:-}