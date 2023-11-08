import React, { useState, useEffect } from "react";
import { Button, TextInput } from "@tremor/react";
import { MagnifyingGlassIcon } from "@heroicons/react/24/outline";
const REACT_APP_SCRAPESTORM_API_KEY = process.env.REACT_APP_SCRAPESTORM_API_KEY;
const REACT_APP_SCRAPESTORM_API_USER =
  process.env.REACT_APP_SCRAPESTORM_API_USER;
const REACT_APP_SCRAPESTORM_API_MEDIA =
  process.env.REACT_APP_SCRAPESTORM_API_MEDIA;
const REACT_APP_SCRAPESTORM_API_TIMEOUT =
  process.env.REACT_APP_SCRAPESTORM_API_TIMEOUT;
const SESSION_STORAGE_USER_PREFIX = "insta_user_";

const Dashboard = () => {
  const [searchText, setSearchText] = useState<string>("");
  const [instaName, setInstaName] = useState<string>("");

  const api_get = (): object => {
    let result: object = {};

    return result;
  };
  const get_str = (input: any): string => {
    if (typeof input === "string") {
      return input;
    }
    return "";
  };
  useEffect(() => {
    if (instaName !== "") {
      console.log("api:" + REACT_APP_SCRAPESTORM_API_USER);

      let result: object;

      const storageLabel = SESSION_STORAGE_USER_PREFIX + instaName;
      let data: string = get_str(sessionStorage.getItem(storageLabel));

      if (data === "") {
        result = api_get();
        sessionStorage.setItem(storageLabel, JSON.stringify(result));
        console.log("saved");
      } else {
        result = JSON.parse(data);
        console.log("loaded");
      }
      console.log(result);
    }
    return () => {
      // Perform any clean-up or unsubscribe actions here
    };
  }, [instaName]);

  const handleSearch = () => {
    // console.log("search: " + searchText);
    setInstaName(searchText);
  };

  const handleSearchTextChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    // console.log(e.target.value);
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
