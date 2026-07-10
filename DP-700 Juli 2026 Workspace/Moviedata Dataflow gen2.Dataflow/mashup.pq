[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared Moviedata2023 = let
  Source = Web.BrowserContents("https://www.boxofficemojo.com/year/2023"),
  #"Extracted table from HTML" = Html.Table(Source, {{"Column0", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(1)"}, {"Column1", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(2)"}, {"Column2", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(3)"}, {"Column3", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(4)"}, {"Column4", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(5)"}, {"Column5", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(6)"}, {"Column6", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(7)"}, {"Column7", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(8)"}, {"Column8", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(9)"}, {"Column9", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(10)"}, {"Column10", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(11)"}}, [RowSelector = "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR"]),
  #"Promoted headers" = Table.PromoteHeaders(#"Extracted table from HTML", [PromoteAllScalars = true]),
  #"Replaced value" = Table.ReplaceValue(#"Promoted headers", "-", null, Replacer.ReplaceValue, {"Gross"}),
  #"Replaced value 1" = Table.ReplaceValue(#"Replaced value", "-", null, Replacer.ReplaceValue, {"Theaters"}),
  #"Replaced value 2" = Table.ReplaceValue(#"Replaced value 1", "-", null, Replacer.ReplaceValue, {"Total Gross"}),
  #"Changed column type" = Table.TransformColumnTypes(#"Replaced value 2", {{"Rank", Int64.Type}, {"Gross", Currency.Type}, {"Total Gross", Currency.Type}, {"Estimated", type logical}}),
  #"Added custom" = Table.AddColumn(#"Changed column type", "Year", each 2023),
  #"Changed column type 1" = Table.TransformColumnTypes(#"Added custom", {{"Year", type text}}),
  #"Added custom 1" = Table.AddColumn(#"Changed column type 1", "Released", each [Release Date] & " " & [Year]),
  #"Changed column type 2" = Table.TransformColumnTypes(#"Added custom 1", {{"Released", type date}}),
  #"Removed columns" = Table.RemoveColumns(#"Changed column type 2", {"Year", "Release Date", "Genre", "Running Time", "Budget"}),
  #"Changed column type 3" = Table.TransformColumnTypes(#"Removed columns", {{"Theaters", Int64.Type}}),
  #"Removed columns 1" = Table.RemoveColumns(#"Changed column type 3", {"Estimated"})
in
  #"Removed columns 1";
shared Moviedata = let
  Source = Web.BrowserContents("https://www.boxofficemojo.com/year/" & year),
  #"Extracted table from HTML" = Html.Table(Source, {{"Column0", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(1)"}, {"Column1", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(2)"}, {"Column2", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(3)"}, {"Column3", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(4)"}, {"Column4", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(5)"}, {"Column5", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(6)"}, {"Column6", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(7)"}, {"Column7", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(8)"}, {"Column8", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(9)"}, {"Column9", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(10)"}, {"Column10", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(11)"}}, [RowSelector = "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR"]),
  #"Promoted headers" = Table.PromoteHeaders(#"Extracted table from HTML", [PromoteAllScalars = true]),
  #"Replaced value" = Table.ReplaceValue(#"Promoted headers", "-", null, Replacer.ReplaceValue, {"Gross"}),
  #"Replaced value 1" = Table.ReplaceValue(#"Replaced value", "-", null, Replacer.ReplaceValue, {"Theaters"}),
  #"Replaced value 2" = Table.ReplaceValue(#"Replaced value 1", "-", null, Replacer.ReplaceValue, {"Total Gross"}),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"Rank", Int64.Type}, {"Gross", Currency.Type}, {"Total Gross", Currency.Type}, {"Estimated", type logical}}),
  #"Added custom" = Table.AddColumn(#"Changed column type", "Year", each year),
  #"Changed column type 1" = Table.TransformColumnTypes(#"Added custom", {{"Year", type text}}),
  #"Added custom 1" = Table.AddColumn(#"Changed column type 1", "Released", each [Release Date] & " " & [Year]),
  #"Replaced value 3" = Table.ReplaceValue(#"Added custom 1", "- " & year, null, Replacer.ReplaceValue, {"Released"}),
  #"Changed column type 2" = Table.TransformColumnTypes(#"Replaced value 3", {{"Released", type date}}),
  #"Removed columns" = Table.RemoveColumns(#"Changed column type 2", {"Year", "Release Date", "Genre", "Running Time", "Budget"}),
  #"Changed column type 3" = Table.TransformColumnTypes(#"Removed columns", {{"Theaters", Int64.Type}}),
  #"Removed columns 1" = Table.RemoveColumns(#"Changed column type 3", {"Estimated"})
in
  #"Removed columns 1";
shared year = "2024" meta [IsParameterQuery = true, IsParameterQueryRequired = false, Type = type text];
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "MovieDataAllYears_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "Year", DestinationColumnName = "Year"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared MovieDataAllYears = let
  MovieDataAllYears = {2020 .. 2026},
  #"Converted to table" = Table.FromList(MovieDataAllYears, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
  #"Renamed columns" = Table.RenameColumns(#"Converted to table", {{"Column1", "Year"}}),
  #"Changed column type" = Table.TransformColumnTypes(#"Renamed columns", {{"Year", type text}}),
  #"Invoked custom function" = Table.AddColumn(#"Changed column type", "Invoked custom function", each GetMovieData([Year])),
  #"Expanded Invoked custom function" = Table.ExpandTableColumn(#"Invoked custom function", "Invoked custom function", {"Rank", "Release", "Gross", "Theaters", "Total Gross", "Distributor", "Released"}, {"Rank", "Release", "Gross", "Theaters", "Total Gross", "Distributor", "Released"})
in
  #"Expanded Invoked custom function";
[FunctionQueryBinding = "{""exemplarFormulaName"":""Moviedata""}"]
shared GetMovieData = (year as text) => let
  Source = Web.BrowserContents("https://www.boxofficemojo.com/year/" & year),
  #"Extracted table from HTML" = Html.Table(Source, {{"Column0", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(1)"}, {"Column1", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(2)"}, {"Column2", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(3)"}, {"Column3", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(4)"}, {"Column4", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(5)"}, {"Column5", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(6)"}, {"Column6", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(7)"}, {"Column7", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(8)"}, {"Column8", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(9)"}, {"Column9", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(10)"}, {"Column10", "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR > :nth-child(11)"}}, [RowSelector = "TABLE.a-bordered.a-horizontal-stripes.a-size-base.a-span12.mojo-body-table.mojo-table-annotated.mojo-body-table-compact.scrolling-data-table > * > TR"]),
  #"Promoted headers" = Table.PromoteHeaders(#"Extracted table from HTML", [PromoteAllScalars = true]),
  #"Replaced value" = Table.ReplaceValue(#"Promoted headers", "-", null, Replacer.ReplaceValue, {"Gross"}),
  #"Replaced value 1" = Table.ReplaceValue(#"Replaced value", "-", null, Replacer.ReplaceValue, {"Theaters"}),
  #"Replaced value 2" = Table.ReplaceValue(#"Replaced value 1", "-", null, Replacer.ReplaceValue, {"Total Gross"}),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"Rank", Int64.Type}, {"Gross", Currency.Type}, {"Total Gross", Currency.Type}, {"Estimated", type logical}}),
  #"Added custom" = Table.AddColumn(#"Changed column type", "Year", each year),
  #"Changed column type 1" = Table.TransformColumnTypes(#"Added custom", {{"Year", type text}}),
  #"Added custom 1" = Table.AddColumn(#"Changed column type 1", "Released", each [Release Date] & " " & [Year]),
  #"Replaced value 3" = Table.ReplaceValue(#"Added custom 1", "- " & year, null, Replacer.ReplaceValue, {"Released"}),
  #"Changed column type 2" = Table.TransformColumnTypes(#"Replaced value 3", {{"Released", type date}}),
  #"Removed columns" = Table.RemoveColumns(#"Changed column type 2", {"Year", "Release Date", "Genre", "Running Time", "Budget"}),
  #"Changed column type 3" = Table.TransformColumnTypes(#"Removed columns", {{"Theaters", Int64.Type}}),
  #"Removed columns 1" = Table.RemoveColumns(#"Changed column type 3", {"Estimated"})
in
  #"Removed columns 1";
shared MovieDataAllYears_DataDestination = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "."]}[Data],
  Navigation_2 = Navigation_1{[displayName = "CITirsdagDataWarehouse"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "bronze"]}[Data],
  TableNavigation = Navigation_3{[Name = "MovieDataAllYear"]}?[Data]?
in
  TableNavigation;
