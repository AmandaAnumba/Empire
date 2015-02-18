module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        
        // compiling sass files to css with compass
        compass: {
            dev: {
                options: {
                    config: 'config.rb',
                    outputStyle: 'compressed',
                    noLineComments:true, 
                }
            }
        },

        // bundling all of the require() calls and js files into a 
        // bundle.js/module.js file
        browserify: {
            home: {
                files: {
                    'app/static/js/build.js': ['test/**/*.js'],
                }
            },
            articles: {
                files: {
                    'app/static/js/build.js': ['test/**/*.js'],
                }
            },
            users: {
                files: {
                    'app/static/js/users.dist.js': ['app/static/js/s3uploader.js'],
                }
            },
            dist: {
                files: {
                    'app/static/js/build.js': ['test/**/*.js'],
                }
            }
        },

        // minify js files
        uglify: {
            options: {
                sourceMap: false,
                banner: '/*! main.js \n all functions required for empire functionality \n <%= grunt.template.today("m-d-yy") %> */\n\n'
            },
            prod: {
                files: {
                    'app/static/js/prod/main.min.js': ['app/static/js/main.js']
                }
            },
        },

        // minify css files
        cssmin: {
            target: {
                files: {
                    'css/dist/built.min.css': ['css/base.css', 'css/mocha.css']
                }
            }
        },

        watch: {
            styles: {
                files: ['app/static/stylesheets/modules/**/*.scss','app/static/stylesheets/partials/**/*.scss'],
                tasks: ['compass:dev'],
                options: {
                    spawn: false,
                },
            },
        },
    });
    
    // Load the plugin that provides the each task.
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-browserify');

    // create a task and run it by typing 'grunt lint' on the command line
    grunt.registerTask('prod', ['jshint:all']);
    
    // on watch events configure jshint:all to only run on changed file
    grunt.event.on('watch', function(action, filepath) {
        grunt.config('compass', filepath);
    });

    // Default task(s) to run by typing 'grunt' on the command line
    grunt.registerTask('default', ['watch']);
};