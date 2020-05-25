#!/bin/sh

pulumi login file:///.pulumi

pulumi ${@:-}