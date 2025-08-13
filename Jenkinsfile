pipeline {
//     agent any  // Запускает на любом доступном агенте
    agent {
        dockerfile {
            filename 'Dockerfile'  // Использует Dockerfile из репозитория
        }
    }

    stages {
        // 1. Получение кода из Git
        stage('Checkout') {
            steps {
                checkout scm  // Клонирует репозиторий
            }
        }

        // 2. Установка зависимостей Python
        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        // 3. Запуск тестов (pytest)
        stage('Test') {
            steps {
                sh 'pytest tests/ --verbose'  // Путь к тестам
            }
//             post {
//                 always {
//                     junit '**/test-results.xml'  // Сохраняет отчеты (если pytest генерирует JUnit-формат)
//                 }
//             }
        }

        // 4. Проверка стиля кода (опционально)
//         stage('Lint') {
//             steps {
//                 sh 'pylint src/'  // Проверка стиля
//             }
//         }
    }

    // Уведомления о результате
    post {
        always {
            echo 'Pipeline завершен!'
        }
//         success {
//             slackSend channel: '#dev-team', message: '✅ Pipeline успешно выполнен!'
//         }
//         failure {
//             slackSend channel: '#dev-team', message: '❌ Pipeline упал! Проверьте логи.'
//         }
    }
}