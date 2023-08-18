import { Construct } from 'constructs';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';

export class LambdaStack extends Construct {
  constructor(scope: Construct, id: string) {
    super(scope, id);


    const handler = new Function(this, '', {
      runtime: Runtime.PYTHON_3_10,
      code: Code.fromAsset('../app.zip'),
      handler: 'lambdas/martyred_model_trainer.handler',
      environment: {}
    });
  }
}