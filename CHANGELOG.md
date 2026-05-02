# Changelog

## 1.10.0 (2026-05-02)

Full Changelog: [v1.9.0...v1.10.0](https://github.com/CASParser/cas-parser-python/compare/v1.9.0...v1.10.0)

### Features

* **api:** api update ([809f3de](https://github.com/CASParser/cas-parser-python/commit/809f3de0c92ab34db2ffcdcc494adaba9913fe7a))
* **api:** api update ([4aa46fc](https://github.com/CASParser/cas-parser-python/commit/4aa46fcbc1cf3279f572ff3a1c2110a6e1f31d4a))

## 1.9.0 (2026-05-01)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/CASParser/cas-parser-python/compare/v1.8.0...v1.9.0)

### Features

* support setting headers via env ([cddcbfe](https://github.com/CASParser/cas-parser-python/commit/cddcbfeb1bc2304e73bc00e209a36e54835bff65))


### Bug Fixes

* use correct field name format for multipart file arrays ([f944611](https://github.com/CASParser/cas-parser-python/commit/f9446112d528f85c0b81de683fb920173ccd419f))


### Chores

* **internal:** more robust bootstrap script ([058a8e9](https://github.com/CASParser/cas-parser-python/commit/058a8e9da54a73314e16eb650e8e45e3982cc677))
* **internal:** reformat pyproject.toml ([c619569](https://github.com/CASParser/cas-parser-python/commit/c619569d3b418561dc076a8e6eb11a080479e34e))

## 1.8.0 (2026-04-19)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/CASParser/cas-parser-python/compare/v1.7.0...v1.8.0)

### Features

* **api:** api update ([78f7f97](https://github.com/CASParser/cas-parser-python/commit/78f7f97e1f17e44bc4443c43e92baf1888b2808a))
* **api:** api update ([2e57117](https://github.com/CASParser/cas-parser-python/commit/2e571178acf86c879c727a43cff97ab4e05c1e2d))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([3e5eea1](https://github.com/CASParser/cas-parser-python/commit/3e5eea1e92928bd98243022c607f6f15afa24d52))
* ensure file data are only sent as 1 parameter ([4985a34](https://github.com/CASParser/cas-parser-python/commit/4985a349eee6f59007dfdf770c26deba75acc7dd))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([1c854af](https://github.com/CASParser/cas-parser-python/commit/1c854af1baa2f1e702881692b65e9a85efffedd5))

## 1.7.0 (2026-03-27)

Full Changelog: [v1.6.3...v1.7.0](https://github.com/CASParser/cas-parser-python/compare/v1.6.3...v1.7.0)

### Features

* **internal:** implement indices array format for query and form serialization ([80766b1](https://github.com/CASParser/cas-parser-python/commit/80766b13d42f7b06973be98f5e2eb9e62fd411d8))


### Bug Fixes

* sanitize endpoint path params ([83a2f2c](https://github.com/CASParser/cas-parser-python/commit/83a2f2c62dc993603487e8b19b6e329b7475510e))


### Chores

* **ci:** skip lint on metadata-only changes ([dec3e9b](https://github.com/CASParser/cas-parser-python/commit/dec3e9bf8d1857ae839eca13cbe76f6146845d31))
* **internal:** update gitignore ([c5e98a4](https://github.com/CASParser/cas-parser-python/commit/c5e98a45887d92948399e3be7c7f0bcacf68b5cf))

## 1.6.3 (2026-03-17)

Full Changelog: [v1.6.2...v1.6.3](https://github.com/CASParser/cas-parser-python/compare/v1.6.2...v1.6.3)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([f287f8f](https://github.com/CASParser/cas-parser-python/commit/f287f8fa5bd9a7bc28ee45fb5eb5bc88ed15efd6))
* **pydantic:** do not pass `by_alias` unless set ([194da96](https://github.com/CASParser/cas-parser-python/commit/194da969949332a8e76968bdce5ddd5c24aa4eab))


### Chores

* **internal:** tweak CI branches ([5f370c3](https://github.com/CASParser/cas-parser-python/commit/5f370c3cf3447548fa4e801de902efa881043788))

## 1.6.2 (2026-03-07)

Full Changelog: [v1.6.1...v1.6.2](https://github.com/CASParser/cas-parser-python/compare/v1.6.1...v1.6.2)

### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([a3b3292](https://github.com/CASParser/cas-parser-python/commit/a3b329233e5e5f10acd8aad8d888de2112475af1))

## 1.6.1 (2026-03-03)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/CASParser/cas-parser-python/compare/v1.6.0...v1.6.1)

### Chores

* **ci:** bump uv version ([8b38574](https://github.com/CASParser/cas-parser-python/commit/8b38574493387605ea62763e2dac86b90cb41697))
* **internal:** add request options to SSE classes ([7488011](https://github.com/CASParser/cas-parser-python/commit/74880111923232fba22d9870f00aabf17cd7ef2f))
* **internal:** codegen related update ([b9079a9](https://github.com/CASParser/cas-parser-python/commit/b9079a9473681d297cfdd4165e2aae413d784bfd))
* **internal:** make `test_proxy_environment_variables` more resilient ([3608c6e](https://github.com/CASParser/cas-parser-python/commit/3608c6eddf68e65c153c4e186346b79859aab866))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([60ab278](https://github.com/CASParser/cas-parser-python/commit/60ab27826aeea8d2b9dc6ec19f8a94bc4108b180))
* **internal:** refactor authentication internals ([deb70b3](https://github.com/CASParser/cas-parser-python/commit/deb70b3a007f6596260f115d964f69cd55b456c3))

## 1.6.0 (2026-02-23)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/CASParser/cas-parser-python/compare/v1.5.0...v1.6.0)

### Features

* **api:** manual updates ([6551087](https://github.com/CASParser/cas-parser-python/commit/6551087fbe4480228ebfd967674eddf89c006684))

## 1.5.0 (2026-02-23)

Full Changelog: [v1.4.1...v1.5.0](https://github.com/CASParser/cas-parser-python/compare/v1.4.1...v1.5.0)

### Features

* **api:** api update ([8a5eeaa](https://github.com/CASParser/cas-parser-python/commit/8a5eeaa3334343c0a5e8268d06c0c25d7dfdef00))
* **api:** api update ([478ce0c](https://github.com/CASParser/cas-parser-python/commit/478ce0c2535de083e5c6f9248d0df77e6bafb410))
* **api:** api update ([dcf866c](https://github.com/CASParser/cas-parser-python/commit/dcf866c9577a219abb273e5b34e2c95bda3404f2))
* **api:** manual updates ([a4d6336](https://github.com/CASParser/cas-parser-python/commit/a4d6336829387e982ac938935252129ff5131f65))

## 1.4.1 (2026-02-20)

Full Changelog: [v1.4.0...v1.4.1](https://github.com/CASParser/cas-parser-python/compare/v1.4.0...v1.4.1)

### Chores

* **internal:** remove mock server code ([582f64d](https://github.com/CASParser/cas-parser-python/commit/582f64db76f09909f2c406877633b3db56b492dc))
* update mock server docs ([d2942ae](https://github.com/CASParser/cas-parser-python/commit/d2942aef06e12bb1e57040358b68555f7e28bf15))

## 1.4.0 (2026-02-14)

Full Changelog: [v1.3.2...v1.4.0](https://github.com/CASParser/cas-parser-python/compare/v1.3.2...v1.4.0)

### Features

* **api:** manual updates ([5026d18](https://github.com/CASParser/cas-parser-python/commit/5026d18984d879743658d9ff7b4e0be698694db4))
* **api:** manual updates ([ae2a833](https://github.com/CASParser/cas-parser-python/commit/ae2a8339e530187bbf543fc8f4b34d04ac2bc8e2))

## 1.3.2 (2026-02-14)

Full Changelog: [v1.3.1...v1.3.2](https://github.com/CASParser/cas-parser-python/compare/v1.3.1...v1.3.2)

### Chores

* update SDK settings ([285da6c](https://github.com/CASParser/cas-parser-python/commit/285da6c1583452aaaf7806375bdae5e37949bf43))
* update SDK settings ([b5d1609](https://github.com/CASParser/cas-parser-python/commit/b5d16092ea43f7971055d11e98dfb6fab7ee3fe9))
* update SDK settings ([6edc712](https://github.com/CASParser/cas-parser-python/commit/6edc71271e8cd252ec12faac438f81f149c45056))

## 1.3.1 (2026-02-14)

Full Changelog: [v1.3.0...v1.3.1](https://github.com/CASParser/cas-parser-python/compare/v1.3.0...v1.3.1)

### Chores

* configure new SDK language ([1349249](https://github.com/CASParser/cas-parser-python/commit/13492498f165a4c6aa35b0798ecee6ac21ba45d7))

## 1.3.0 (2026-02-14)

Full Changelog: [v1.2.1...v1.3.0](https://github.com/CASParser/cas-parser-python/compare/v1.2.1...v1.3.0)

### Features

* **api:** manual updates ([98b1422](https://github.com/CASParser/cas-parser-python/commit/98b1422eadacacd06a45ffe4ce7dcab0e2dc9f1b))


### Chores

* update SDK settings ([7fcfc93](https://github.com/CASParser/cas-parser-python/commit/7fcfc935a8b94a8ad6401336cc52f9fe66ae3022))
* update SDK settings ([32181ec](https://github.com/CASParser/cas-parser-python/commit/32181ecb3c8bb0e523506b159320422ef565c411))

## 1.2.1 (2026-02-14)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/CASParser/cas-parser-python/compare/v1.2.0...v1.2.1)

### Chores

* update SDK settings ([0231f54](https://github.com/CASParser/cas-parser-python/commit/0231f540b484945a3bbc5d023a11197913e56642))

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
