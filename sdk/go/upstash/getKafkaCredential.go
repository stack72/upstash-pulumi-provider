// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package upstash

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-upstash/sdk/go/upstash"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/upstash/upstash-pulumi-provider/sdk/go/upstash"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := upstash.LookupKafkaCredential(ctx, &GetKafkaCredentialArgs{
// 			CredentialId: upstash_kafka_credential.ExampleKafkaCredential.Credential_id,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupKafkaCredential(ctx *pulumi.Context, args *LookupKafkaCredentialArgs, opts ...pulumi.InvokeOption) (*LookupKafkaCredentialResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupKafkaCredentialResult
	err := ctx.Invoke("upstash:index/getKafkaCredential:getKafkaCredential", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKafkaCredential.
type LookupKafkaCredentialArgs struct {
	CredentialId string `pulumi:"credentialId"`
}

// A collection of values returned by getKafkaCredential.
type LookupKafkaCredentialResult struct {
	ClusterId      string `pulumi:"clusterId"`
	CreationTime   int    `pulumi:"creationTime"`
	CredentialId   string `pulumi:"credentialId"`
	CredentialName string `pulumi:"credentialName"`
	// The provider-assigned unique ID for this managed resource.
	Id          string `pulumi:"id"`
	Password    string `pulumi:"password"`
	Permissions string `pulumi:"permissions"`
	State       string `pulumi:"state"`
	Topic       string `pulumi:"topic"`
	Username    string `pulumi:"username"`
}

func LookupKafkaCredentialOutput(ctx *pulumi.Context, args LookupKafkaCredentialOutputArgs, opts ...pulumi.InvokeOption) LookupKafkaCredentialResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupKafkaCredentialResult, error) {
			args := v.(LookupKafkaCredentialArgs)
			r, err := LookupKafkaCredential(ctx, &args, opts...)
			var s LookupKafkaCredentialResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupKafkaCredentialResultOutput)
}

// A collection of arguments for invoking getKafkaCredential.
type LookupKafkaCredentialOutputArgs struct {
	CredentialId pulumi.StringInput `pulumi:"credentialId"`
}

func (LookupKafkaCredentialOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKafkaCredentialArgs)(nil)).Elem()
}

// A collection of values returned by getKafkaCredential.
type LookupKafkaCredentialResultOutput struct{ *pulumi.OutputState }

func (LookupKafkaCredentialResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKafkaCredentialResult)(nil)).Elem()
}

func (o LookupKafkaCredentialResultOutput) ToLookupKafkaCredentialResultOutput() LookupKafkaCredentialResultOutput {
	return o
}

func (o LookupKafkaCredentialResultOutput) ToLookupKafkaCredentialResultOutputWithContext(ctx context.Context) LookupKafkaCredentialResultOutput {
	return o
}

func (o LookupKafkaCredentialResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

func (o LookupKafkaCredentialResultOutput) CreationTime() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) int { return v.CreationTime }).(pulumi.IntOutput)
}

func (o LookupKafkaCredentialResultOutput) CredentialId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.CredentialId }).(pulumi.StringOutput)
}

func (o LookupKafkaCredentialResultOutput) CredentialName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.CredentialName }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupKafkaCredentialResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupKafkaCredentialResultOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.Password }).(pulumi.StringOutput)
}

func (o LookupKafkaCredentialResultOutput) Permissions() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.Permissions }).(pulumi.StringOutput)
}

func (o LookupKafkaCredentialResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.State }).(pulumi.StringOutput)
}

func (o LookupKafkaCredentialResultOutput) Topic() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.Topic }).(pulumi.StringOutput)
}

func (o LookupKafkaCredentialResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaCredentialResult) string { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupKafkaCredentialResultOutput{})
}
