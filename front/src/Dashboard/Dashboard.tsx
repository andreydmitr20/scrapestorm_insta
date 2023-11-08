import React, { useState, useEffect } from "react";
import { Button } from "@tremor/react";
import { MagnifyingGlassIcon } from "@heroicons/react/24/outline";

const Dashboard = () => {
  const [searchText, setSearchText] = useState<string>("");

  useEffect(() => {
    return () => {
      // Perform any clean-up or unsubscribe actions here
      console.log("Clean-up");
    };
  }, [searchText]);

  const handleSearch = () => {};

  const handleSearchTextChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
    setSearchText(e.target.value);
  };

  return (
    <div className="flex flex-col  justify-center items-center">
      <div className="border-b-2 border-red-500 pb-2">
        <input
          type="text"
          value={searchText}
          onChange={handleSearchTextChange}
        />
        <Button
          className="text-white m-4"
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
