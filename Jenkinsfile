try {
           timeout(time: 20, unit: 'MINUTES') {
              node('nodejs') {
                  stage('build-web') {
                    openshiftBuild(buildConfig: 'app', showBuildLogs: 'true')
                  }
                  stage('deploy-web') {
                    openshiftDeploy(deploymentConfig: 'app')
                  }
                  stage('test-app') {
                      
                      openshiftDeploy(deploymentConfig: 'selenium2')

                  }
                }
           }
        } catch (err) {
           echo "in catch block"
           echo "Caught: ${err}"
           currentBuild.result = 'FAILURE'
           throw err
        }          
