// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;                     // Specifying the Solidity Pragma Version

contract SmartLandscapeMonitoring {         // Smart Landscape Monitoring Contract

    struct LocationInfo {                   // Structure to hold Location Information
        string location;                    // Location name or description      
        int256 latitude;   // multiplied by 1e6 to simulate float
        int256 longitude;                   // Longitude value, multiplied by 1e6 to simulate float
        uint256 elevationMeters;            // Elevation in Meters
    }

    struct EnvironmentData {                // Structure to hold Environmental Data
        string vegetationType;              // Type of vegetation (e.g. grass, shrubs, trees)
        uint256 densityOfVegetation;        // Density of vegetation in square meters
        uint256 soilMoisture;               // Soil moisture percentage
        uint256 temperatureC;               // Temperature in Celsius
        uint256 humidityPercent;            // Humidity percentage
        uint256 windSpeedKph;               // Wind speed in kilometers per hour    
        uint256 sunlightHours;              // Number of sunlight hours per day 
        string weatherCondition;            // Current weather condition (e.g. sunny, rainy, cloudy)
        uint256 environmentalImpactAssessmentScore; // Score for environmental impact assessment
    }

    struct FinancialData {                  // Structure to hold Financial Data
        uint256 budgetAllocatedPhp;         // Budget allocated in Philippine Pesos
        uint256 contractAmountPhp;          // Contract amount in Philippine Pesos
        uint256 depositPhp;                 // Deposit amount in Philippine Pesos   
        uint256 withdrawPhp;                // Withdrawn amount in Philippine Pesos          
        uint256 balanceCheckerPhp;          // Balance checker in Philippine Pesos  
        uint8 paymentStatus;                // e.g. 0 = pending, 1 = paid, 2 = failed
    }

    struct ProjectDetails {                 // Structure to hold Project Details
        string projectType;                 // Type of project (e.g. landscaping, irrigation, maintenance)
        uint8 projectStatus; // e.g. 0 = planning, 1 = ongoing, 2 = completed
        uint256 waterUsageLiters;
        bool maintenanceRequired;
        string landscapeArchitectId;
        string owner;
        string designer;
    }

    struct Project {                        // Structure to hold Project Information
        uint256 timestamp;  
        string projectId;
        LocationInfo locationInfo;
        EnvironmentData environmentData;
        FinancialData financialData;
        ProjectDetails projectDetails;
    }

    mapping(string => Project) public projects;                 // Mapping to store projects by their ID
    string[] public projectIds;

    event ProjectCreated(string projectId, uint256 timestamp);  // Event to log project creation

    function createProject(                                     // Function to create a new project
        string memory _projectId,
        LocationInfo memory _locationInfo,
        EnvironmentData memory _environmentData,
        FinancialData memory _financialData,
        ProjectDetails memory _projectDetails
    ) public {
        require(bytes(projects[_projectId].projectId).length == 0, "Project ID already exists");    // Ensure project ID is unique

        Project memory newProject = Project({                   // Create a new project instance
            timestamp: block.timestamp,
            projectId: _projectId,
            locationInfo: _locationInfo,
            environmentData: _environmentData,
            financialData: _financialData,
            projectDetails: _projectDetails
        });

        projects[_projectId] = newProject;                      // Store the new project in the mapping 
        projectIds.push(_projectId);                            // Add the project ID to the list of project IDs    

        emit ProjectCreated(_projectId, block.timestamp);       // Emit an event for project creation. This allows external applications to listen for project creation events.
    }

    function getProject(string memory _projectId) public view returns (Project memory) {        // Function to retrieve a project by its ID
        require(bytes(projects[_projectId].projectId).length != 0, "Project does not exist");
        return projects[_projectId];
    }

    function getAllProjectIds() public view returns (string[] memory) {         // Function to retrieve all project IDs
        return projectIds;
    }
}
