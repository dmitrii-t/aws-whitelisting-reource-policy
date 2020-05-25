ifeq (pulumi,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  PULUMI_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(PULUMI_ARGS):;@:)
endif

.PHONY: pulumi
pulumi:
	docker-compose run pulumi $(PULUMI_ARGS)

.PHONY: build
build:
	docker-compose build --no-cache pulumi

.PHONY: venv
venv:
	if [ ! -d .venv ]; then python3 -m venv .venv; fi

.PHONY: pip_install
pip_install:
	. .venv/bin/activate; pip install -r requirements.txt

.PHONY: setup
setup: venv pip_install clean

.PHONY: clean
clean:
	rm -rf .pulumi/ && mkdir .pulumi
