{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    utils,
  }: let
    out = system: let
      pkgs = import nixpkgs {
        inherit system;
        config = {
          allowBroken = true;
          allowUnfree = true;
        };
      };
      inherit (pkgs) mkShell poetry2nix python39;
      inherit (poetry2nix) mkPoetryApplication mkPoetryEnv;
      python = python39;
      overrides = pyfinal: pyprev: let
        inherit (pyprev) buildPythonPackage fetchPypi;
      in rec {
        altair-data-server = buildPythonPackage rec {
          pname = "altair_data_server";
          version = "0.4.1";
          src = fetchPypi {
            inherit pname version;
            hash = "sha256-s5IFpIqyZ4Ag/FhznLlzhFh57Racta3d3J3L9aaa6ys=";
          };
          propagatedBuildInputs = with pyfinal; [
            altair
            portpicker
            pytest
            tornado
          ];
        };
        altair-viewer = buildPythonPackage rec {
          pname = "altair_viewer";
          version = "0.4.0";
          src = fetchPypi {
            inherit pname version;
            hash = "sha256-9dM993XLkJRUTxXptXiCJEiPUGz1RscImA0tRML5NTQ=";
          };

          buildInputs = with pyfinal; [
            altair-data-server
            ipython
            pytest
          ];
        };
        altair-saver = buildPythonPackage rec {
          pname = "altair_saver";
          version = "0.5.0";
          src = fetchPypi {
            inherit pname version;
            hash = "sha256-wJi89oaOO6EdsQiQTcO4UVtUUFuJvKX2lScRVIe4h5U=";
          };
          propagatedBuildInputs = with pyfinal; [
            altair-data-server
            altair-viewer
            pillow
            pypdf2
            selenium
          ];
        };
        cython = pyprev.cython.overridePythonAttrs (old: rec {
          version = "0.29.32";
          src = fetchTarball {
            url = "https://files.pythonhosted.org/packages/4c/76/1e41fbb365ad20b6efab2e61b0f4751518444c953b390f9b2d36cf97eea0/Cython-0.29.32.tar.gz";
            sha256 = "sha256:1ysmnfb36635imzkwvxp6v9b7dp8rskf9z7jqydd5hk8zil45lb9";
          };
        });
        dollar-lambda = pyprev.dollar-lambda.overridePythonAttrs (old: {
          buildInputs = old.buildInputs or [] ++ [pyfinal.poetry];
        });
        gql = pyprev.gql.overridePythonAttrs (old: {
          propagatedBuildInputs =
            (old.propagatedBuildInputs or [])
            ++ (with pyfinal; [
              requests
              requests_toolbelt
            ]);
        });
        hatchling = pyprev.hatchling.overridePythonAttrs (old: {
          src = fetchPypi {
            inherit (old) pname;
            version = "1.9.0";
            hash = "sha256-tXxzYvQ3uUJuS5QiiiHSrFgE+7KrywGt3iVEo1uzA80=";
          };
        });
        idna = pyprev.idna.overridePythonAttrs (old: {
          buildInputs = (old.buildInputs or []) ++ [pyfinal.flit-core];
        });
        jsonschema = pyprev.jsonschema.overridePythonAttrs (old: {
          buildInputs =
            (old.buildInputs or [])
            ++ [pyfinal.hatch-fancy-pypi-readme];
        });
        pytypeclass = pyprev.pytypeclass.overridePythonAttrs (old: {
          buildInputs = old.buildInputs or [] ++ [pyfinal.poetry];
        });
        run-logger = pyprev.run-logger.overridePythonAttrs (old: {
          buildInputs = old.buildInputs or [] ++ [pyfinal.poetry];
        });
      };
      poetryArgs = {
        inherit python;
        projectDir = ./.;
        overrides = poetry2nix.overrides.withDefaults overrides;
      };
      poetryEnv = mkPoetryEnv poetryArgs;
      buildInputs = with pkgs; [
        texlive.combined.scheme-full
        chromedriver
        poetry
        poetryEnv
      ];
    in rec {
      devShell = mkShell rec {
        inherit buildInputs;
        PYTHONBREAKPOINT = "ipdb.set_trace";
      };
    };
  in
    utils.lib.eachDefaultSystem out;
}
