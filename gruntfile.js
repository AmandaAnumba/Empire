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

        watch: {
            styles: {
                files: ['app/static/stylesheets/modules/**/*.scss','app/static/stylesheets/partials/**/*.scss'],
                tasks: ['compass'],
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

    // create a task and run it by typing 'grunt lint' on the command line
    // grunt.registerTask('<task_name', ['jshint:all']);
    
    // on watch events configure jshint:all to only run on changed file
    grunt.event.on('watch', function(action, filepath) {
        grunt.config('jshint.all.src', filepath);
    });

    // Default task(s) to run by typing 'grunt' on the command line
    grunt.registerTask('default', ['watch']);
};