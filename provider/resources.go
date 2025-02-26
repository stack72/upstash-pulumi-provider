// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package upstash

import (
	"path/filepath"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/upstash/terraform-provider-upstash/upstash"
	"github.com/upstash/upstash-pulumi-provider/provider/pkg/version"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "upstash"
	// modules:
	mainMod = "index" // the upstash module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
// Delete this altogether.
// func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
// 	return nil
// }

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(upstash.Provider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "upstash",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "Upstash",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "Upstash",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		// Point to some logo... Will add later...
		LogoURL: "https://upstash.com/static/logo/logo-light.svg",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "https://github.com/upstash/upstash-pulumi-provider/releases/download/v${VERSION}",
		Description:       "A Pulumi package for creating and managing upstash cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:   []string{"pulumi", "upstash", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.upstash.com",
		Repository: "https://github.com/upstash/upstash-pulumi-provider",
		// The GitHub Org for the provider - defaults to `terraform-providers`
		GitHubOrg: "upstash",
		Config:    map[string]*tfbridge.SchemaInfo{},
		// delete this one also...
		// PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"upstash_redis_database": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "RedisDatabase"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"password": {
						Secret: tfbridge.True(),
					},
				},
			},
			"upstash_kafka_cluster": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "KafkaCluster"),
			},
			"upstash_kafka_topic": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "KafkaTopic"),
			},
			"upstash_kafka_credential": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "KafkaCredential"),
			},
			"upstash_team": {
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "Team"),
			},
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			// "aws_iam_role": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "IamRole")}
			//
			// "aws_acm_certificate": {
			// 	Tok: tfbridge.MakeResource(mainPkg, mainMod, "Certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: tfbridge.MakeType(mainPkg, "Tags")},
			// 	},
			// },
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"upstash_redis_database_data": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getRedisDatabase"),
			},
			"upstash_kafka_cluster_data": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getKafkaCluster"),
			},
			"upstash_kafka_topic_data": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getKafkaTopic"),
			},
			"upstash_kafka_credential_data": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getKafkaCredential"),
			},
			"upstash_team_data": {
				Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getTeam"),
			},
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAmi")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@upstash/pulumi",
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "upstash_pulumi",
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				"github.com/upstash/upstash-pulumi-provider/sdk/",
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "Pulumi",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
