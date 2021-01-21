import pulumi
from pulumi_azure import core, storage, appservice

# Resource Group
pulumi_rg = core.ResourceGroup('pulumi_rg')

# App Service Plan
pulumi_plan = appservice.Plan("pulumiPlan",
    location=pulumi_rg.location,
    resource_group_name=pulumi_rg.name,
    sku=appservice.PlanSkuArgs(
        tier="Standard",
        size="S1",
    ))

# Web App
pulumi_app_service = appservice.AppService("pulumiAppService",
    location=pulumi_rg.location,
    resource_group_name=pulumi_rg.name,
    app_service_plan_id=pulumi_plan.id,
    app_settings={
        "ENVIRONMENT": "dev",
    },
)

# Export the hostname for the web app
pulumi.export('hostname', pulumi_app_service.default_site_hostname)
