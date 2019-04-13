app.config(function($routeProvider,$locationProvider)
          {
    $locationProvider.hashPrefix('');
    
    $routeProvider.when("/",{
        templateUrl:"clothes.html"
    }).when("/mobile",{
        templateUrl:"mobile.html"
    }).when("/shoes",{
        templateUrl:"shoes.html"
    }).when("/clothes",{
        templateUrl:"clothes.html"
    }).otherwise({template:"hahah",redirectTo:"/"});
    
    
    
    
}
);