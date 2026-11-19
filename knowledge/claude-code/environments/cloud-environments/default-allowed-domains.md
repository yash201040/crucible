---
type: "Reference"
title: "Default allowed domains"
description: "Domains reachable under Limited network access with Allow package managers checked, grouped by category."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, allowlist, domains, package-managers]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: ""
identifiers:
  - "api.anthropic.com"
  - "github.com"
  - "registry.npmjs.org"
  - "pypi.org"
  - "crates.io"
  - "proxy.golang.org"
  - "registry-1.docker.io"
  - "ghcr.io"
  - "*.amazonaws.com"
  - "*.googleapis.com"
  - "*.modelcontextprotocol.io"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The default allowlist applies at **Limited** access while **Allow package managers** is checked (the default for a new environment). `*` marks wildcard subdomain matching.

# How to use it

| Category | Domains |
| - | - |
| Anthropic services | api.anthropic.com, docs.claude.com, platform.claude.com, code.claude.com, claude.ai, claude.com, support.claude.com, anthropic.com, www.anthropic.com |
| Version control | github.com, www.github.com, api.github.com, npm.pkg.github.com, raw.githubusercontent.com, pkg-npm.githubusercontent.com, objects.githubusercontent.com, release-assets.githubusercontent.com, codeload.github.com, avatars.githubusercontent.com, camo.githubusercontent.com, gist.github.com, gitlab.com, www.gitlab.com, registry.gitlab.com, bitbucket.org, www.bitbucket.org, api.bitbucket.org |
| Container registries | registry-1.docker.io, auth.docker.io, index.docker.io, hub.docker.com, www.docker.com, production.cloudflare.docker.com, production.cloudfront.docker.com, download.docker.com, gcr.io, *.gcr.io, ghcr.io, mcr.microsoft.com, *.data.mcr.microsoft.com, public.ecr.aws |
| Cloud platforms | cloud.google.com, accounts.google.com, gcloud.google.com, *.googleapis.com, storage/compute/container.googleapis.com, azure.com, portal.azure.com, microsoft.com, www.microsoft.com, *.microsoftonline.com, packages.microsoft.com, dotnet.microsoft.com, dot.net, visualstudio.com, dev.azure.com, *.amazonaws.com, *.api.aws, oracle.com, www.oracle.com, java.com, www.java.com, java.net, www.java.net, download.oracle.com, yum.oracle.com, *.r2.cloudflarestorage.com |
| JavaScript/Node | registry.npmjs.org, www.npmjs.com, www.npmjs.org, npmjs.com, npmjs.org, yarnpkg.com, registry.yarnpkg.com, jsr.io, npm.jsr.io |
| Python | pypi.org, www.pypi.org, files.pythonhosted.org, pythonhosted.org, test.pypi.org, pypi.python.org, pypa.io, www.pypa.io |
| Ruby | rubygems.org, www.rubygems.org, api.rubygems.org, index.rubygems.org, ruby-lang.org, www.ruby-lang.org, rubyforge.org, www.rubyforge.org, rubyonrails.org, www.rubyonrails.org, rvm.io, get.rvm.io |
| Rust | crates.io, www.crates.io, index.crates.io, static.crates.io, rustup.rs, static.rust-lang.org, www.rust-lang.org |
| Go | proxy.golang.org, sum.golang.org, index.golang.org, golang.org, www.golang.org, goproxy.io, pkg.go.dev |
| JVM | maven.org, repo.maven.org, central.maven.org, repo1.maven.org, repo.maven.apache.org, maven.google.com, jcenter.bintray.com, gradle.org, www.gradle.org, services.gradle.org, plugins.gradle.org, plugins-artifacts.gradle.org, kotlinlang.org, www.kotlinlang.org, spring.io, repo.spring.io |
| Other package managers | packagist.org, www.packagist.org, repo.packagist.org (PHP); nuget.org, www.nuget.org, api.nuget.org (.NET); pub.dev, api.pub.dev (Dart); hex.pm, www.hex.pm (Elixir); cpan.org, www.cpan.org, metacpan.org, www.metacpan.org, api.metacpan.org (Perl); cocoapods.org, www.cocoapods.org, cdn.cocoapods.org; haskell.org, www.haskell.org, hackage.haskell.org; swift.org, www.swift.org |
| Linux distributions | archive.ubuntu.com, security.ubuntu.com, ubuntu.com, www.ubuntu.com, *.ubuntu.com, ppa.launchpad.net, launchpad.net, www.launchpad.net, *.nixos.org |
| Dev tools and platforms | dl.k8s.io, pkgs.k8s.io, k8s.io, www.k8s.io, releases.hashicorp.com, apt/rpm/archive.releases.hashicorp.com, hashicorp.com, www.hashicorp.com, repo.anaconda.com, conda.anaconda.org, anaconda.org, www.anaconda.com, anaconda.com, continuum.io, apache.org, www.apache.org, archive.apache.org, downloads.apache.org, eclipse.org, www.eclipse.org, download.eclipse.org, nodejs.org, www.nodejs.org, developer.apple.com, developer.android.com, pkg.stainless.com, binaries.prisma.sh |
| Monitoring | http-intake.logs.datadoghq.com, *.datadoghq.com, *.datadoghq.eu, api.honeycomb.io |
| Content delivery | sourceforge.net, *.sourceforge.net, packagecloud.io, *.packagecloud.io, fonts.googleapis.com, fonts.gstatic.com |
| Schema and configuration | json-schema.org, www.json-schema.org, json.schemastore.org, www.schemastore.org |
| Model Context Protocol | *.modelcontextprotocol.io |

# Notes

The .NET SDK and similar toolchains are not pre-installed even though their registries are on this list.
