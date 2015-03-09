module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        watch: {
            styles: {
                files: ['app/static/stylesheets/**/*.scss'],
                tasks: ['compass'],
                options: {
                    spawn: false,
                    livereload: true,
                },
            },
            grunt: {
                files: ['gruntfile.js']
            }
        },

        uglify: {
            files: [{
                expand: true,              
                cwd: 'app/static/js/',       
                src: ['**/*.js', '!**/*.min.js', '!bootstrap/**/*.js', '!trash.js', '!bootstrap-sprockets.js'], 
                dest: 'app/static/js/prod/', 
                ext: '.min.js',             
                extDot: 'last'             
            }],
        },

        compass: {
            options: {
                config: 'config.rb'
            },
            expand: true,
            cwd: 'app/static/stylesheets/',
            src: ['sass/**/*.scss'], 
            dest: 'app/static/stylesheets/css/',
            ext: '.css',
            extDot: 'last',          
        },

        copy: {
            backup: {
                expand: true, 
                cwd: 'production/', 
                src: ['**'], 
                dest: 'production.bak/',
            },
            prod: {
                files: [
                    // virtual environment
                    {expand: true, cwd: 'macEnv/', src: ['**'], dest: 'production/macEnv/'},

                    // images
                    {expand: true, cwd: 'app/static/images/', src: ['**'], dest: 'production/static/images/'},

                    // javascript
                    {expand: true, cwd: 'app/static/js/prod/', src: ['**'], dest: 'production/static/js/'},

                    // plugins
                    {expand: true, cwd: 'app/static/plugins/', src: ['**'], dest: 'production/static/plugins/'},

                    // stylesheets
                    {expand: true, cwd: 'app/static/stylesheets/css/', src: ['**'], dest: 'production/static/stylesheets/css/'},

                    // templates
                    {expand: true, cwd: 'app/static/templates/', src: ['**'], dest: 'production/templates/'},

                    // blueprints
                    {expand: true, cwd: 'app/', src: ['content/**', 'dashboard/**', 'user/**', 'application.py'], dest: 'production/'},

                    // other
                    {src: ['requirements.txt', 'config.py'], dest: 'production/'},
                ]
            },
        }, 

        clean: {
            backup: ['production.bak/**/*', '!production.bak/.ebextensions/**'],
            prod: ['production/**/*', '!production/.ebextensions/**'],
        },

        compress: {
            options: {
                archive: 'prod.zip'
            },
            files: {
                src: 'production/**/*',
                dest: '/'
            }
        }
    });
    
    // Load the plugin that provides the each task.
    grunt.loadNpmTasks('grunt-browserify');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-compress');

    // create a task and run it by typing 'grunt lint' on the command line
    grunt.registerTask('backup', ['clean:backup', 'copy:backup']);
    grunt.registerTask('prod', ['backup', 'clean:prod', 'compass', 'uglify', 'copy:prod', 'compress']);
    
    // on watch events configure jshint:all to only run on changed file
    // grunt.event.on('watch', function(action, filepath) {
    //     grunt.config('compass', filepath);
    // });

    // Default task(s) to run by typing 'grunt' on the command line
    grunt.registerTask('default', ['watch']);
};