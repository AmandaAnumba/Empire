var Upload = require('s3-uploader');

var client = new Upload('empire-images', {
	awsBucketUrl: 'https://empire-images.s3.amazonaws.com/',
	awsBucketPath: 'images/',
	awsBucketAcl: 'public-read',
 
	versions: [{
		original: true
	},{
		suffix: '-large',
		quality: 80,
		maxHeight: 1040,
		maxWidth: 1040,
	},{
		suffix: '-medium',
		maxHeight: 780,
		maxWidth: 780
	},{
		suffix: '-small',
		maxHeight: 320,
		maxWidth: 320
	}]
});