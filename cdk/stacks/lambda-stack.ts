import { App, Stack, StackProps } from 'aws-cdk-lib';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';
import { Rule, Schedule } from 'aws-cdk-lib/aws-events';
import { LambdaFunction } from 'aws-cdk-lib/aws-events-targets';

export class LambdaStack extends Stack {
  constructor(scope: App, id: string, props?: StackProps) {
    super(scope, id, props);

    const sainyMartyredModelTrainerFn = new Function(this, 'SainyMartyredModelTrainerFn', {
      runtime: Runtime.PYTHON_3_10,
      code: Code.fromAsset('../app.zip'),
      handler: 'lambdas/martyred_model_trainer.handler',
      environment: {}
    });

    const eventRule = new Rule(this, `${sainyMartyredModelTrainerFn.functionName}`, {
        schedule: Schedule.expression('cron(*/15 * * * *)')
    });

    eventRule.addTarget(new LambdaFunction(sainyMartyredModelTrainerFn))
  }
}