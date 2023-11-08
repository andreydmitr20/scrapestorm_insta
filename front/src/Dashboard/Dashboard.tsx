import React, { useState, useEffect } from "react";
import { Button, TextInput } from "@tremor/react";
import { MagnifyingGlassIcon } from "@heroicons/react/24/outline";

const Dashboard = () => {
  const [searchText, setSearchText] = useState<string>("");

  useEffect(() => {
    return () => {
      // Perform any clean-up or unsubscribe actions here
      console.log("Clean-up");
    };
  }, [searchText]);

  const handleSearch = () => {
    console.log("search: " + searchText);
  };

  const handleSearchTextChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
    setSearchText(e.target.value);
  };

  const handleOnKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <div className="flex flex-col justify-center items-center w-full">
      <div className="flex flex-row mx-4 w-full ">
        <TextInput
          className="m-2"
          type="text"
          placeholder="Search..."
          value={searchText}
          onChange={handleSearchTextChange}
          onKeyPress={handleOnKeyPress}
        />
        <Button
          className="m-2"
          size="sm"
          onClick={handleSearch}
          variant="primary"
          icon={MagnifyingGlassIcon}
        >
          Search
        </Button>
      </div>
      <div className="border-b-2 border-red-100 pb-2">
        <h1>222</h1>
      </div>
    </div>
  );
};

export default Dashboard;
