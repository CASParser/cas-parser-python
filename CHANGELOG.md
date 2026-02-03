# Changelog

## 1.2.0 (2026-02-03)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/CASParser/cas-parser-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([bce15d3](https://github.com/CASParser/cas-parser-python/commit/bce15d3f55a18db8d0c6447b6537fbdf831a5816))
* **api:** api update ([c265056](https://github.com/CASParser/cas-parser-python/commit/c265056c6b8f5b346172d89e9da82315976dc44f))
* **api:** api update ([93a9613](https://github.com/CASParser/cas-parser-python/commit/93a9613c79ec70869cf11dd0b9bac0a8c6194a31))
* **api:** api update ([bd6977a](https://github.com/CASParser/cas-parser-python/commit/bd6977a8a78c4a1633e4e6a1dc1d3335b1aa6611))
* **api:** api update ([3fda81d](https://github.com/CASParser/cas-parser-python/commit/3fda81deb938a9b689cbb04f839e3b815259a9c5))
* **api:** api update ([f1838dc](https://github.com/CASParser/cas-parser-python/commit/f1838dcb901635626cc87cb55dfaa4ef33ba5092))


### Bug Fixes

* **client:** close streams without requiring full consumption ([7090ef5](https://github.com/CASParser/cas-parser-python/commit/7090ef51af296fa6d6be8af8137543ef2023cbd7))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([e1b65fb](https://github.com/CASParser/cas-parser-python/commit/e1b65fb2bd146a68ef50438899406ae2fb6178c3))
* do not install brew dependencies in ./scripts/bootstrap by default ([35b17eb](https://github.com/CASParser/cas-parser-python/commit/35b17eb26264ab66e24b074bcb1790f6c33b7b9c))
* **internal/tests:** avoid race condition with implicit client cleanup ([2a58fc0](https://github.com/CASParser/cas-parser-python/commit/2a58fc0e260b52ee314ac6d14676b2140711bd0b))
* **internal:** codegen related update ([8e6c5b2](https://github.com/CASParser/cas-parser-python/commit/8e6c5b210e14602af113fa9fef5c789d6238419a))
* **internal:** codegen related update ([20bcea0](https://github.com/CASParser/cas-parser-python/commit/20bcea057ce1974149394c899581ed31ffb56a4a))
* **internal:** detect missing future annotations with ruff ([8c35489](https://github.com/CASParser/cas-parser-python/commit/8c354893c00887af1da9c197dc21dd4d6f0033af))
* **internal:** grammar fix (it's -&gt; its) ([d2d29bc](https://github.com/CASParser/cas-parser-python/commit/d2d29bcc46989573e27c2178785c6b38df65bd90))
* **internal:** update pydantic dependency ([1c3104b](https://github.com/CASParser/cas-parser-python/commit/1c3104b27350f4c906973bb56f89d5a16f55d35e))
* **types:** change optional parameter type from NotGiven to Omit ([e739e12](https://github.com/CASParser/cas-parser-python/commit/e739e12ade4f91e52f0285c866354e970195aacf))

## 1.1.0 (2025-09-06)

Full Changelog: [v1.0.2...v1.1.0](https://github.com/CASParser/cas-parser-python/compare/v1.0.2...v1.1.0)

### Features

* improve future compat with pydantic v3 ([39d5f4a](https://github.com/CASParser/cas-parser-python/commit/39d5f4a6f631f01627f9e0ad3846431b2f36410d))
* **types:** replace List[str] with SequenceNotStr in params ([ffdac79](https://github.com/CASParser/cas-parser-python/commit/ffdac79d2ac8394afc09f540c6b89c01675946d9))


### Chores

* **internal:** add Sequence related utils ([cffd684](https://github.com/CASParser/cas-parser-python/commit/cffd6844655dfe7f52a1c85140dc4ab2a370e8f7))
* **internal:** move mypy configurations to `pyproject.toml` file ([2f7e6bc](https://github.com/CASParser/cas-parser-python/commit/2f7e6bccf82f65c0b753a909654ba1ee7cc61157))
* **tests:** simplify `get_platform` test ([7c54665](https://github.com/CASParser/cas-parser-python/commit/7c546655385360b8ba97e20e79fbdedb43af07d5))

## 1.0.2 (2025-08-27)

Full Changelog: [v1.0.1...v1.0.2](https://github.com/CASParser/cas-parser-python/compare/v1.0.1...v1.0.2)

### Bug Fixes

* avoid newer type syntax ([2ad1ea6](https://github.com/CASParser/cas-parser-python/commit/2ad1ea633d5c9d69de09045f97968aa961ccc6f3))


### Chores

* **internal:** change ci workflow machines ([f38494c](https://github.com/CASParser/cas-parser-python/commit/f38494c9f9f0df5069d8dd1ff23728a47f0e934c))
* **internal:** update pyright exclude list ([d3f9237](https://github.com/CASParser/cas-parser-python/commit/d3f9237f030f0087d0f92741836aa8674d9b5287))
* update github action ([83a551a](https://github.com/CASParser/cas-parser-python/commit/83a551a025d281efa4edaa89a9e4daed0f8aaa8e))

## 1.0.1 (2025-08-18)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/CASParser/cas-parser-python/compare/v1.0.0...v1.0.1)

### Chores

* update SDK settings ([83e97ee](https://github.com/CASParser/cas-parser-python/commit/83e97eef5fe5c02d181c8eeea271f661cd4b8830))

## 1.0.0 (2025-08-18)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/CASParser/cas-parser-python/compare/v0.0.1...v1.0.0)

### Features

* **api:** manual updates ([635bd26](https://github.com/CASParser/cas-parser-python/commit/635bd26431623f00d3af06a3256c2b7085c83487))


### Chores

* configure new SDK language ([5748dab](https://github.com/CASParser/cas-parser-python/commit/5748dab8b8241dc537456d9b8c1dae3c0e4a5d5a))
* update SDK settings ([13b5c47](https://github.com/CASParser/cas-parser-python/commit/13b5c470a31ac72d95078236e0e16b76e753939e))
* update SDK settings ([25126eb](https://github.com/CASParser/cas-parser-python/commit/25126eb2330f0e84bd4dd9e814e6a2e5b2ebbddc))
