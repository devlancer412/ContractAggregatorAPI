const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Ballot", function () {
  it("Should return the new greeting once it's changed", async function () {
    const Ballot = await ethers.getContractFactory("Ballot");
    const ballot = await Ballot.deploy(["Rama", "Nick", "Jose"]);
    await ballot.deployed();
  });
});
