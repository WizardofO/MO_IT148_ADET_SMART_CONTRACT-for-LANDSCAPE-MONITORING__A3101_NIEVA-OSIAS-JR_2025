// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SmartLandscapeMonitoring {

    struct LocationInfo {
        string location;
        int256 latitude;   // multiplied by 1e6 to simulate float
        int256 longitude;
        uint256 elevationMeters;
    }

    struct EnvironmentData {
        string vegetationType;
        uint256 densityOfVegetation;
        uint256 soilMoisture;
        uint256 temperatureC;
        uint256 humidityPercent;
        uint256 windSpeedKph;
        uint256 sunlightHours;
        string weatherCondition;
        uint256 environmentalImpactAssessmentScore;
    }

    struct FinancialData {
        uint256 budgetAllocatedPhp;
        uint256 contractAmountPhp;
        uint256 depositPhp;
        uint256 withdrawPhp;
        uint256 balanceCheckerPhp;
        uint8 paymentStatus; // e.g. 0 = pending, 1 = paid, 2 = failed
    }

    struct ProjectDetails {
        string projectType;
        uint8 projectStatus; // e.g. 0 = planning, 1 = ongoing, 2 = completed
        uint256 waterUsageLiters;
        bool maintenanceRequired;
        string landscapeArchitectId;
        string owner;
        string designer;
    }

    struct Project {
        uint256 timestamp;
        string projectId;
        LocationInfo locationInfo;
        EnvironmentData environmentData;
        FinancialData financialData;
        ProjectDetails projectDetails;
    }

    mapping(string => Project) public projects;
    string[] public projectIds;

    // Mapping to prevent duplicate LocationInfo
    mapping(bytes32 => bool) private usedLocationHashes;

    event ProjectCreated(string projectId, uint256 timestamp);

    function createProject(
        string memory _projectId,
        LocationInfo memory _locationInfo,
        EnvironmentData memory _environmentData,
        FinancialData memory _financialData,
        ProjectDetails memory _projectDetails
    ) public {
        require(bytes(projects[_projectId].projectId).length == 0, "Project ID already exists");

        // Compute hash of LocationInfo and check for duplicates
        bytes32 locationHash = getLocationHash(_locationInfo);
        require(!usedLocationHashes[locationHash], "Duplicate location data");

        Project memory newProject = Project({
            timestamp: block.timestamp,
            projectId: _projectId,
            locationInfo: _locationInfo,
            environmentData: _environmentData,
            financialData: _financialData,
            projectDetails: _projectDetails
        });

        projects[_projectId] = newProject;
        projectIds.push(_projectId);

        // Mark location as used
        usedLocationHashes[locationHash] = true;

        emit ProjectCreated(_projectId, block.timestamp);
    }

    function getProject(string memory _projectId) public view returns (Project memory) {
        require(bytes(projects[_projectId].projectId).length != 0, "Project does not exist");
        return projects[_projectId];
    }

    function getAllProjectIds() public view returns (string[] memory) {
        return projectIds;
    }

    function getLocationHash(LocationInfo memory loc) internal pure returns (bytes32) {
        return keccak256(abi.encodePacked(loc.location, loc.latitude, loc.longitude, loc.elevationMeters));
    }
}
