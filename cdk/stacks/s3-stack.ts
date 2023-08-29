import { App, Stack, StackProps } from 'aws-cdk-lib';



export class S3Stack extends Stack {
  constructor(scope: App, id: string, props?: StackProps) {
    super(scope, id, props);

    const {
      MODELS_DIRECTORY_NAME,
      COLUMN_TRANSFORMERS_DIRECTORY_NAME,
    } = process.env


  }
}
