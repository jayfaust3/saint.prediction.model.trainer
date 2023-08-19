import { App, Stack, StackProps } from 'aws-cdk-lib';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';

export class LambdaStack extends Stack {
  constructor(scope: App, id: string, props?: StackProps) {
    super(scope, id, props);

    const sainyMartyredModelTrainerFn = new Function(this, 'SainyMartyredModelTrainerFn', {
      runtime: Runtime.PYTHON_3_10,
      code: Code.fromAsset('../app.zip'),
      handler: 'lambdas/martyred_model_trainer.handler',
      environment: {}
    });

    // const instanceActionPolicy = 
  }
}